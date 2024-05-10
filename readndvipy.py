# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:00:05 2021

@author: Per

"""


### Good reading about how to read files line by line
# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

import numpy as np
import matplotlib.pyplot as plt
 
# Using readline() to read one line at a time
file1 = open('./wa/ndvilistwa.txt', 'r')
count = 0
 
fig, ax = plt.subplots() 

# Dimension total matrix
C = np.zeros((200,200,108))

while True:
    count += 1
 
    # Get next line from file
    line = "./wa/" + file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break

       
    if count > 1:
        A = np.fromfile(line.strip(), dtype=np.uint8,count=40000) # count=40000
        A.shape = (200,200)
        # Build a 200 x 200 x 108 matrix
        C[:,:,count-2] = A[:,:]
        pos = ax.imshow(A,vmin=120,vmax=250,cmap="jet")
        cb = plt.colorbar(pos)
      #  fig.colorbar(pos)
        plt.pause(0.1)
        file = "./wa/image%i.pdf" %(count) 
        ax.set_title("Image %i" %(count-1))
 #       fig.savefig(file)
        cb.remove()
        ax.cla()
    print("Line{}: {}".format(count, line.strip()))
 
file1.close()

# Now extract and display

fig, ax = plt.subplots()
for i in np.arange(199,0,-1):
   print(i)
   v = C[i,100,:]
   ax.plot(v)
   ax.axis([0,108,120,250]) 
   plt.pause(0.1)
   file = "ts%i.pdf" %(199-i) 
   ax.set_title("Row %i" %(i))
#   fig.savefig(file)
   ax.cla()
