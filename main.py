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
from scipy.interpolate import Rbf

 
# Using readline() to read one line at a time
file1 = open('./wa/ndvilistwa.txt', 'r')
maxCount = int(file1.readline())
window = 4

Index1 = 36
#Extra Indices for rolling mean window
Index2 = 71 + window - 1
pointsList = []

_low = 44
_high = 61 
# Dimension total matrix
C = np.zeros((200,200,Index2-Index1))

minimas = []
maximas = []

def ImageAnalysis(Animate, count, ax): 
    # Get next line from file
    line = "./wa/" + file1.readline()
    A = np.fromfile(line.strip(), dtype=np.uint8,count=40000) # count=40000
    A.shape = (200,200)
    
    # Build a 200 x 200 x 108 matrix
    C[:,:,count-Index1] = A[:,:]
    
    if count == _low or count == _high:
        x, y = np.meshgrid(np.arange(200), np.arange(200))
        #z = np.full_like(x, count - Index1)
        pts = []
        pts.extend(zip(x.flatten(), y.flatten(), A.flatten()))
        pointsList.append(pts)
    
    if Animate: 
        fig, ax = plt.subplots()
        pos = ax.imshow(A,vmin=120,vmax=250,cmap="jet")
        cb = plt.colorbar(pos)
        
        plt.pause(0.3)
        ax.set_title("Image %i" %(count))
        
        cb.remove()
        ax.cla()
        print("Line{}: {}".format(count, line.strip()))

def CreateMapAnimation(Animate): 
    
    if Animate:
        fig, ax = plt.subplots()
        
    if not Animate: 
        ax = 0
        
    for count in range(Index1, Index2):
        ImageAnalysis(Animate, count, ax)
    plt.close() 
    file1.close()


def CreateTimeSeriesAnimation(Animate, Condense): 
    if Animate or Condense:
        fig, ax = plt.subplots()
    for a in np.arange(199, 0, -1):
        for i in np.arange(199,0,-1): # From Atlantic ocean to the
            
            v = C[i,a,:] # Extract time-series
            #ax.plot(v) # Plot time-series
            #Skip data that has no vegetation index
            if(np.mean(v) < 120):
                continue
            
            #Calculate Rolling Mean 
            avg_data = []
            for ind in range(len(v) - window + 1):
                avg_data.append(np.mean(v[ind:ind+window]))
            
            #Median Attempt
            #avg_data.append(v[0])
            #for ind in range(1, len(v) - window): 
            #    avg_data.append(np.median((v[ind-2], v[ind], v[ind+2])))
            #avg_data.append(v[-1])
            
            #Spline 
            spl = UnivariateSpline(np.arange(36,71, step = 1),avg_data)
            xs = np.linspace(Index1, Index2-window, 1000)
            spl.set_smoothing_factor(1000)
            #spl.set_smoothing_factor(2000)
            listSpl = spl(xs).tolist()
                
            #Establish peaks and dips 
            minimas.append(xs[listSpl.index(min(listSpl))])
            maximas.append(xs[listSpl.index(max(listSpl))])
            if Condense and i%3 == 0 and a%3 == 0: 
                #ax.plot(np.arange(Index1,Index2-window+1, step = 1), avg_data)
                ax.plot(xs, spl(xs), 'g', lw=3, alpha = 0.002)
                ax.axis([Index1, Index2-window,120,250])
            if Animate: 
                #Original Data Plot
                #ax.plot(np.arange(36,71, step = 1), v[0:35])
                print(i) # Saharan border'
                ax.plot(np.arange(Index1,Index2-window+1, step = 1), avg_data)
                ax.plot(xs, spl(xs), 'g', lw=3)
                ax.axis([Index1, Index2-window,120,250])
                plt.pause(0.1)
                ax.cla()
    if Condense: 
        plt.show() 

def plot_3d_scatter(pt):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    points = pt 
    points = [point for point in points if point[2] >= 30]
    xs, ys, zs = zip(*points)
    xs = xs[::30]
    ys = ys[::30]
    zs = zs[::30]
    
    #sc = ax.scatter(xs[::15], ys[::15], zs[::15], c = zs[::15], cmap='jet', marker='o')
    x, y = np.meshgrid(xs, ys)
    print(len(x) == len(y) == len(zs))
    rbf = Rbf(x, y, zs, function="quintic") 
    Z_pred = rbf(x, y) 
    #ax.plot_surface(xs, ys, zs) 
    ax.plot_surface(x, y, Z_pred) 
    plt.show()
    #plt.colorbar(sc)
    ax.set_zlim(120,250)
    plt.show()


#Needed to create data for timeseries,  1st param determines if animation is created 
CreateMapAnimation(False)
plot_3d_scatter(pointsList[0])
#plot_3d_scatter(pointsList[1])
CreateTimeSeriesAnimation(False, False)
print(np.median(maximas))
print(np.median(minimas))








    

