# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:00:05 2021

@author: Per

"""


### Good reading about how to read files line by line
# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
 
# Using readline() to read one line at a time
file1 = open('./wa/ndvilistwa.txt', 'r')
maxCount = int(file1.readline())
fig, ax = plt.subplots() 

# Dimension total matrix
C = np.zeros((200,200,108))

def ImageAnalysis(Animate): 
    # Get next line from file
    line = "./wa/" + file1.readline()
    A = np.fromfile(line.strip(), dtype=np.uint8,count=40000) # count=40000
    A.shape = (200,200)
    
    # Build a 200 x 200 x 108 matrix
    C[:,:,count-2] = A[:,:]
    #pos = ax.imshow(A,vmin=120,vmax=250,cmap="jet")
    #cb = plt.colorbar(pos)
    
    #  fig.colorbar(pos)
    if not Animate: 
        return 
    plt.pause(0.02)
    #file = "./wa/image%i.pdf" %(count) 
    ax.set_title("Image %i" %(count-1))
    
    #       fig.savefig(file)
    #cb.remove()
    ax.cla()
    print("Line{}: {}".format(count, line.strip()))
    
for count in range(maxCount):
    ImageAnalysis(False) 
 
file1.close()

# Now extract and display

fig, ax = plt.subplots()
for i in np.arange(163,0,-1): # From Atlantic ocean to the
    print(i) # Saharan border
    v = C[i,100,:] # Extract time-series
    
    ax.plot(v) # Plot time-series
    
    
    spl = UnivariateSpline(np.arange(len(v)),v)
    xs = np.linspace(0, 108, 1000)
    spl.set_smoothing_factor(20000)
    ax.plot(xs, spl(xs), 'g', lw=3)
    ax.axis([0,108,120,250])
    
    plt.pause(0.1)
    ax.set_title("Row %i" %(i))
    ax.cla()

    

