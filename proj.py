# -*- coding: utf-8 -*-
"""
READNDVI.PY
Reads and displays images of NDVI values as an animation
"""
### Good reading about how to read files line by line
# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
import numpy as np
4
import matplotlib.pyplot as plt
# Using readline() to read one line at a time
file1 = open('./wa/clavrlistwa.txt', 'r')
count = 0
fig, ax = plt.subplots()
# Dimension total matrix
C = np.zeros((200,200,108))
while True:
    count += 1
    # Get next line from file
    line = file1.readline()
    # if line is empty end of file is reached
    if not line:
        break
    if count > 1:
        A = np.fromfile(line.strip(), dtype=np.uint8,count=40000) # count=40000
        A.shape = (200,200)
        # Build a 200 x 200 x 108 matrix
        C[:,:,count-2] = A[:,:]
        pos = ax.imshow(A,vmin=120,vmax=250,cmap="jet")
        cb = plt.colorbar(pos)
        plt.pause(0.1)
        ax.set_title("Image %i" %(count-1))
        cb.remove()
        ax.cla()
print("Line{}: {}".format(count, line.strip()))
file1.close()