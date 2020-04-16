import os, string
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
#%%
def plot_images_SEM_short():
    folder = "SEM_short/"
    images = os.listdir(folder)
    print(images)
    
    fig = plt.figure(figsize=[14,10]) # set image size
    plt.subplots_adjust(wspace = 0.7, hspace=0.7)# set distance between the subplots
    
    i = 0
    for image in images:
        plt.subplot(2,2,i+1)
        im = plt.imread(folder+image, format='.tiff')
        i+=1
        imgplot = plt.imshow(im)
        plt.axis('off')
    for i, label in enumerate(('a', 'b', 'c', 'd')):
        ax = fig.add_subplot(2,2,i+1)
        ax.text(-.025, 0.95, label, transform=ax.transAxes,
                fontsize=25, fontweight='bold', va='top', ha='right')    
    
    plt.tight_layout()
    plt.draw()
    plt.savefig('SEM_short.png',bbox_inches='tight')
    plt.show()
    return
#%%
def plot_images_SEM():
    folder = "SEM/"
    images = os.listdir(folder)
    print(images)
    
    fig = plt.figure(figsize=[14,10]) # set image size
    plt.subplots_adjust(wspace = 0.15)# set distance between the subplots
    plt.rcParams["font.family"] = "Times New Roman"
    
    i = 0
    for image in images:
        ax = plt.subplot(1,2,i+1)
        im = plt.imread(folder+image, format='.png')
        i+=1
        imgplot = plt.imshow(im)
        plt.axis('off')
    for i, label in enumerate(('a', 'b')):
        ax = fig.add_subplot(1,2,i+1)
        ax.text(-0.025, 0.95, label, transform=ax.transAxes,
                fontsize=25, fontweight='bold', va='top', ha='right') 
        
    plt.tight_layout()
    plt.draw()
    plt.savefig('SEM.png',bbox_inches='tight')
    plt.show()
    return
#%%
