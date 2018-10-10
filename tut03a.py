import numpy as np
import matplotlib.pyplot as plt

############################################################
#NUMPY TUTORIAL 03(a)
############################################################
#Task: load ZnO.xye and replot using a rolling average to get a better
#signal-to-noise ratio

#Load data here (as per 01a):
fpath = '/home/tomwood/Documents/Misc/numpy-tutorials/ZnO.xye'
data = np.loadtxt(fpath)

def fig_setup(figsize=(10, 10)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    return fig, ax

#Write a function that takes data and a number of datapoints (n) and returns
#a new version of data (length = len(data) - 2n), where each point, data[i]
#in data[n:-n] has been averaged over the range data[i-n:i+n+1]. The new
#version of data returned should have x and y columns only (not e). Use said
#function to produce rolling averages of the data with n=2 and n=5 and plot
#together with the original data. Put a legend on your plot, so that it's
#clear which dataset is which.

#def rolling_average(data, n):
