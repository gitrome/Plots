import datetime  # For finding system's real time
import json  # For serializing and deserializing parameters on configuration file.
import re  # For regular expression support
import serial.tools.list_ports  # For listing available serial ports
import serial  # For serial communication
import signal  # For trapping ctrl-c or SIGINT
import sys  # For reading command-line arguments and exiting program with exit code
import time  # For delaying in seconds
import urllib.parse  # For encoding data to be url safe.
import urllib.request  # send data to online server
import platform # For detecting operating system flavor and computer architecture
# import os # For running command line commands
"""
SDI-12 Sensor Data Logger Copyright Dr. John Liu
*019-02-07 Backported feature from 1.6.1: list serial port handles onboard serial port properly (no serial # for onboard serial ports).
2018-07-09 Implemented command-line arguments parser.
    Implemented argument cfg:config_file_name. It overrides the default config file name so the script can be executed with different configurations.
    Added opening port by ID feature in parameters and saving port ID to config file in interactive session.
2018-07-03 Improved exception handling for the SDI-12 protocol. No response from the sensor will not trigger exception.
    Rather, the loop waits for the next iteration and try again. Time to read line 274
2018-04-24 Added exception handling for opening a non-existing serial port (possibly the config file has wrong port name).
    Added exception handling for http.client.BadStatusLine from urllib calls.
2018-04-21 Tested recently added features such as D0, D1, and M, M1.
2018-04-19 Updated the script to issue multiple commands such as M and M1.
    Added features to collect all data using D0, D1, etc. until it collects all measurements
    No longer asks for analog sensors. Just type in address z with the other sensors and issue
    commands 0 or 1 to collect single-ended or differential analog channels from SDI-12 + Analog adapter.
    The script saves a configuration file Liudrlogger.conf. You can modify it with a text editor.
    It's very easy to understand. With the config file, the logger starts in auto-logging mode.
    If you delete the file, it starts interactive session to gather the parameters from the user.
2018-04-07 Replaced capitalize() with upper. Added urllib.error.URLError to exception handling.
    Commented out os and platform imports and unit_id.
    Decoded byte strings before converting into float to stay compatible with MicroPython.
2018-03-29 Added exception handling for urllib.request.urlopen for server internal error
2018-03-28 Replaced cURL with urllib.request for sending data to thingspeak.com server
2017-11-06 Updated telemetry code to upload to thingspeak.com from data.sparkfun.com.
2017-06-23 Added exception handling in case the SDI-12 + GPS USB adapter doesn't return any data (no GPS lock).
    Added serial port and file closing in ctrl + C handler.
2017-02-02 Added multiple-sensor support. Just type in multiple sensor addresses when asked for addresses.
    Changed sdi_12_address into regular string from byte string.
    I found out that byte strings when iterated over becomes integers.
    It's easy to cast each single character string into byte string with .encode() when needed as address.
    Removed specific analog input code and added the adapter address to the address string instead.
2016-11-12 Added support for analog inputs
2016-07-01 Added .strip() to remove \r from input files typed in windows
    Added Ctrl-C handler
    Added sort of serial port placing FTDI at item 0 if it exists
"""
rev_date = '2018-07-09'
version = '1.6.0'

config_file_name = 'test_ni_3.conf'
# Default values of operating parameters
paras_default = dict([
    ('wifi_ssid', 'datalogger'),
    ('wifi_passwd', 'logger1234'),
    ('my_timezone', 'CET-1CEST'),
    ('channelID', '359964'),
    ('api_key', 'GTOEBKK8ZQHI1V1B'),
    ('total_data_count', 1000),
    ('delay_between_pts', 60),
    ('sdi_12_address', '1'),
    ('sdi_12_command', ['0']),
    ('analog_inputs', '0'),
    ('time_zone_choice', 1),
    ('ser', []),
])

cmd_args_sep=':'
cmd_args={}
arg_config_file_name='cfg'

def process_cmd_args():
    global config_file_name, cmd_args
    if len(sys.argv)>1: # 1 argument => script name
        for i in sys.argv[1:]: # Exclude script name in argument list
            print(i)
            if cmd_args_sep in i: # We have name value pair
                cmd_args[i.split(cmd_args_sep)[0]]=i.split(cmd_args_sep)[1]
            else:
                cmd_args[i]=True # We just have name
        # Find arguments that can be processed
        if arg_config_file_name in cmd_args:
            print('Using config file: %s' %(cmd_args[arg_config_file_name]))
            config_file_name=cmd_args[arg_config_file_name]

def SIGINT_handler(signal, frame):
    ser[0].close()
    data_file.close()
    print('Quitting program!')
    sys.exit(0)


signal.signal(signal.SIGINT, SIGINT_handler)
ser = []  # This list stores opened serial port
fnf = False  # File not found error

# This one for everyone to perform tests with
# channelID = "359964"
# api_key = "GTOEBKK8ZQHI1V1B"

# This one for a specific test
# channelID = '462421'
# api_key = "RYZS3T8ILEMW967J"

# This one for Dr. Liu's demo. Don't use
# channelID = '462583'
# api_key = 'NSRT0JDQWD1A4IMX'

# Use computer name as unit_id. For a raspberry pi, change its name from raspberrypi to something else to avoid confusion
# unit_id=platform.node()

http_request_url_format = 'https://api.thingspeak.com/update/?api_key=%s%s'
max_upload_values = 6  # Maximal values to upload as a single data point
adapter_sdi_12_address = 'z'
# This is the flag to break out of the inner loops and continue the next data point loop in case no data is received from a sensor such as the GPS.
no_data = False
VID_FTDI = 0x0403;
port_device='' # This is the device name to the serial port, such as 'COM3' or '/dev/ttyUSB0'.

def load_paras():
# Load operating parameters from default dictionary.
# The function returns a dictionary, which has keys for all parameters needed in the program.
    try:
        f = open(config_file_name, 'r')
        par = json.load(f)
        f.close()
        return (par, False)  # Return paras and False for file not found
    except FileNotFoundError as e:
        print('No configuration file found. Starting interactive session...')
        return (paras_default, True)  # Return default paras and True for file not found


def print_credit(pa):
    print('+-' * 40)
    print('SDI-12 Sensor and Analog Sensor Python Data Logger with Telemetry V', version)
    print(
        'Designed for Dr. Liu\'s family of SDI-12 USB adapters (standard,analog,GPS)\n\tDr. John Liu Saint Cloud MN USA',
        rev_date, '\n\t\tFree software GNU GPL V3.0')
    print('\nCompatible with PCs running Win 7/10, GNU/Linux, Mac OSX, Raspberry PI, Beagle Bone Black')
    print('\nThis program requires Python 3.4, Pyserial 3.0, and internet connector (data upload)')
    print('\nUsing config file:%s' %(config_file_name))
    print('\nData is logged to YYYYMMDD.CVS in the Python code\'s folder')
    print('\nVisit https://thingspeak.com/channels/%s to inspect or retrieve data' % (pa['channelID']))
    print('\nFor assistance with customization, telemetry etc., contact Dr. Liu.')
    print('\nhttps://liudr.wordpress.com/gadget/sdi-12-usb-adapter/')
    print('+-' * 40)


def interactive_session(pa):
    # List ports for user to select

    a = serial.tools.list_ports.comports()
    print('\nDetected the following serial ports:')
    i=0
    for w in a:
        vidn=w.vid if (type(w.vid) is int) else 0
        sern=w.serial_number if (type(w.serial_number) is str) else 'NONE'
        sern=sern[:-1] if ((type(w.vid) is int) and (w.vid==VID_FTDI) and (platform.system()=='Windows')) else sern # Windows OS FTDI driver adds 'A' to the end of the serial number.
        print('%d)\t%s\t(USB VID=%04X)\t Serial#:=%s' % (i, w.device, vidn, sern))
        i=i+1
    total_ports = i  # now i= total ports


    user_port_selection = input('\nSelect port from list (0,1,2...). SDI-12 adapter has USB VID=0403:')
    if (int(user_port_selection) >= total_ports):
        exit(1)  # port selection out of range
    
    port_device=a[int(user_port_selection)].device # Store the device name to later open port with.

    # Store serial port ID
    pa['ser'].append(a[int(user_port_selection)].serial_number if platform.system()!='Windows' else a[int(user_port_selection)].serial_number[:-1])# Windows OS FTDI driver adds 'A' to the end of the serial number.

    # Open serial port
    ser.append(serial.Serial(port=port_device, baudrate=9600, timeout=10))
    time.sleep(2.5)  # delay for arduino bootloader and the 1 second delay of the adapter.

    pa['total_data_count'] = int(input('Total number of data points:'))
    pa['delay_between_pts'] = int(input('Delay between data points (second):'))
    # Enter addresses and commands for each sensor
    pa['sdi_12_address'] = ''
    user_sdi_12_address = input(
        'Enter all SDI-12 sensor addresses as a list, such as 123z.\nIf you have analog channels on your adapter, include address z to your list:')
    pa['sdi_12_address'] = user_sdi_12_address.strip()  # Remove any \r from an input file typed in windows
    pa['sdi_12_command'] = []  # Clear the list of commands
    print('\n\nSensor measurement commands:\nBasic sensors respond to M0 (same as M) command.')
    print(
        'More sophiscated sensors respond to more commands, such as M0 for moisture, and M1 for temperature for an HSTI soil probe.')
    print('\nTo send the basic command M0, enter 0. To send more commands such as M0, M1 and M4, enter 014.')
    for addr in pa['sdi_12_address']:  # Get measurement commands
        print('\nFor SDI-12 sensor %c, which command(s) should be sent?' % (addr))
        pa['sdi_12_command'].append(input('Enter command:'))

    # pa['analog_inputs']=input('Collect analog inputs (requires SDI12-USB + Analog adapter)? (Y/N)')
    # pa['analog_inputs']=(pa['analog_inputs'].strip()).upper() # Remove any \r from an input file typed in windows and capitalize answer
    print('Time stamps are generated with:\n0) GMT/UTC\n1) Local\n')
    pa['time_zone_choice'] = int(input('Select time zone.'))
    f = open(config_file_name, 'w')  # Save settings
    json.dump(paras, f)
    f.close()
    if input('Execute the script? (Y/N)')=='N':
        print('\r\nConfiguration saved to:%s' %(config_file_name))
        print('\r\nTo execute the script with this config file, first change to the directory that contains the script.\r\nMake sure the config file is in the same directory.\r\n\r\nOn GNU/Linux/RPI, enter "python3 script_name cfg:%s"' %(config_file_name))
        print('On Windows, enter "python script_name cfg:%s"' %(config_file_name))
        exit(0);
    

# if len(sdi_12_address)==0:
#    sdi_12_address=adapter_sdi_12_address # Use default address


def sensor_info(pa):
    for an_address in pa['sdi_12_address']:
        ser[0].write(an_address.encode() + b'I!')
        sdi_12_line = ser[0].readline()
        print('Sensor address:', an_address, ' Sensor info:', sdi_12_line.decode('utf-8').strip())

# Main execution starts here
process_cmd_args() # Process command line arguments that may override default values such as config file's name
(paras, fnf) = load_paras()
print_credit(paras)

if (fnf):  # No configuration file. Start interactive session. Serial port is open in the interactive session.
    interactive_session(paras)
else:  # Open serial port
    print('\nUsing saved configuration...\n')
    try: # Open port by ID
        a = serial.tools.list_ports.comports()
        found_port=False
        for w in a:
            if (w.serial_number.__str__()[:len(paras['ser'][0])]==paras['ser'][0]): # Match ID with the correct port
                ser.append(serial.Serial(port=w.device, baudrate=9600, timeout=10))
                time.sleep(2.5)  # Wait for arduino bootloader
                found_port=True
        if not found_port:
            print('Serial port ID in config file not found on system!')
            sys.exit(1)
    except serial.serialutil.SerialException as err:
        print(err.__str__())
        print('Invalid serial port in config file!')
        sys.exit(1)

sensor_info(paras)

# Open data file for logging
if paras['time_zone_choice'] == 0:
    now = datetime.datetime.utcnow()  # use UTC time instead of local time
elif paras['time_zone_choice'] == 1:
    now = datetime.datetime.now()  # use local time, not recommended for multiple data loggers in different time zones

data_file_name = "%s_%04d%02d%02d.csv" % (config_file_name, now.year, now.month, now.day)
data_file = open(data_file_name, 'a')  # open config_file_name_yyyymmdd.csv for appending
print('Saving to %s' % data_file_name)
ser_ptr = 0

for j in range(paras['total_data_count']):
    i = 0  # This counts to max_upload_values to limit data sent to the server.
    value_str = ''  # This stores &value0=xxx&value1=xxx&value2=xxx&value3=xxx&value4=xxx&value5=xxx and is only reset after all sensors are read.
    if paras['time_zone_choice'] == 0:
        now = datetime.datetime.utcnow()
    elif paras['time_zone_choice'] == 1:
        now = datetime.datetime.now()
    output_str = "%04d/%02d/%02d %02d:%02d:%02d%s" % (now.year, now.month, now.day, now.hour, now.minute, now.second,' GMT' if paras['time_zone_choice'] == 0 else '')  # formatting date and time
    for (cmd_ptr, an_address) in enumerate(paras['sdi_12_address']):
        values = []  # clear before each sensor
        sdi_12_line_buffer = b''  # This stores all data from the same sensor address, including from M!->D0! D1!, M1!->D0!, D1! etc.
        for a_command in paras['sdi_12_command'][cmd_ptr]:
            try:
                if a_command == '0':
                    complete_command = an_address.encode() + b'M!'
                else:
                    complete_command = an_address.encode() + b'M' + a_command.encode() + b'!'
                ser[ser_ptr].write(complete_command);  # start the SDI-12 sensor measurement
                # print(complete_command);  # start the SDI-12 sensor measurement
                sdi_12_line = ser[ser_ptr].readline()
                # print(sdi_12_line)
                if sdi_12_line==b'': # Didn't get a response from the sensor? Faulty wiring?
                    print('Sensor %s failed to respond to command %s.' %(an_address,complete_command))
                    no_data = True # End the current iteration of sensors and commands on each sensor and wait for the next iteration.
                    break;
                sdi_12_line = sdi_12_line[:-2]  # remove \r and \n since [0-9]$ has trouble with \r
                m = re.search(b'[0-9]$', sdi_12_line)  # This should match a number ([0-9]) that appears at the end of the response ($), which is a 1-digit number of "returned values" but it is having trouble with the \r so I removed \r\n in the previous line of code.
                if (not m):  # Match evaluates into True. The response is wrong. There should be a number at the end of the response, save \r\n, but it is not in this response.
                    no_data = True # End the current iteration of sensors and commands on each sensor and wait for the next iteration.
                    break;
                total_returned_values = int(m.group(0))  # find out how many values are returned
                # print(total_returned_values)
                sdi_12_line = ser[ser_ptr].readline()  # read the service request line
                if sdi_12_line != an_address.encode() + b'\r\n':
                    print('Sensor %s didn\'t respond with correct service request.' % (an_address))
                    no_data = True  # End the current iteration of sensors and commands on each sensor and wait for the next iteration.
                    break;
                # Read as much data as you can with D0, D1, ... D9 until only the address and \r\n is returned
                for d_command in range(10):
                    complete_command = an_address.encode() + b'D' + str(d_command).encode() + b'!'
                    ser[ser_ptr].write(complete_command)  # request data
                    # print(complete_command)  # request data
                    next_sdi_12_line = ser[ser_ptr].readline()  # read the data line
                    # print(sdi_12_line)
                    if (len(next_sdi_12_line) <= 3): # only 1\r\n is returned, indicating that the sensor has run out of values to return. It's time to stop asking.
                        break
                    else:
                        next_sdi_12_line = next_sdi_12_line[1:-2]  # remove address, \r and \n since [0-9]$ has trouble with \r, stitch all responses from D0! to D9! together for later processing.
                        sdi_12_line_buffer += next_sdi_12_line  # Append results from the Dn! command to data from D0! to Dn-1!
            except serial.serialutil.SerialException as err:
                print(err.__str__())
                ser[ser_ptr].close()
                sys.exit(1)
            # print(sdi_12_line_buffer) # Received data from one address one M command
            for iterator in range(total_returned_values):  # extract the returned values from SDI-12 sensor and append to values[]
                m = re.search(b'[+-][0-9.]+', sdi_12_line_buffer)  # search a number string with preceding + or - sign and any number of digits and decimal (+).
                try:  # if values found is less than values indicated by return from M, report no data found. This is a simple solution to GPS sensors before they acquire lock. For sensors that have lots of values to return, you need to find a better solution.
                    values.append(float(m.group(0).decode()))  # convert into a number. Decode byte string into string first due to MicroPython.
                    sdi_12_line_buffer = sdi_12_line_buffer[len(m.group(0)):]
                except AttributeError:
                    print("No data received from sensor at address %c\n" % (an_address))
                    time.sleep(paras['delay_between_pts'])
                    no_data = True
                    break
            if (no_data == True):
                break;

        output_str = output_str + ',' + an_address

        for value_i in values:
            output_str = output_str + ",%s" % (value_i)  # Output returned values
            if (i < max_upload_values):
                value_str = value_str + "&field%d=%s" % (i + 1, value_i)  # format values for posting. Field starts with field1, not field0.
                i = i + 1
    if (no_data == True):
        no_data = False
        time.sleep(paras['delay_between_pts'])
        continue;
    while (i < max_upload_values):  # Pad with zeros in case we don't have max_upload_values fields. This is only necessary for certain servers.
        value_str = value_str + "&field%d=0" % (i + 1)  # format values for posting. Field starts with field1, not field0.
        i = i + 1

    print(output_str)
    output_str = output_str + '\n'
    data_file.write(output_str)

    http_request_url = http_request_url_format % (paras['api_key'], value_str)  # Format url command
    print(http_request_url)  # Debug information
    try:
        # req = urllib.request.urlopen(http_request_url)
        pass # Enable logging to thingspeak with the previous line. Make sure you get your own thingspeak channel and replace the channel ID and API key.
    except: # Intermittent internet connection could cause more underlying modules to through exceptions. Just catch any exception and discard.
        print("Unexpected error:", sys.exc_info()[0])
    #except (urllib.error.HTTPError, urllib.error.URLError, http.client.BadStatusLine) as err:
        #print('Error uploading data.')
        #print(err.__str__())  # Sometimes the server returns with 500 Internal error and this error is raised and needs to be caught otherwise it breaks the script.
        # You can decide whether to send the request one or a few more times or just discard the error and move on.
    else:
        print('Sent data')
    #print(req.status)  # Send data to server and print out response. 200 means OK.

    values = []  # clear values for the next iteration, 3.2.3 doesn't support clear as 3.4.3 and 3.5.1 does
    data_file.flush()  # make sure data is written to the disk so stopping the scrit with ctrl - C will not cause data loss
    time.sleep(paras['delay_between_pts'])
ser[ser_ptr].close()
data_file.close()
