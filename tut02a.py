import numpy as np
import matplotlib.pyplot as plt

############################################################
#NUMPY TUTORIAL 02(a)
############################################################
#Task: load ZnO.xye and write a function to calculate the area under the
#peaks

#Load data here (as per 01a):
fpath = '/home/tomwood/Documents/Misc/numpy-tutorials/ZnO.xye'
data = np.loadtxt(fpath)

def fig_setup(figsize=(10, 10)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    return fig, ax

#Reusing bits of your code from tut01b, write a function that finds the
#maximum peak and the area under said peak within a certain width. The
#output for find_area(data, width=1.5) should be 43.075
#def area_under_biggest_peak(data, width=1.5):
