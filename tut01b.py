import numpy as np
import matplotlib.pyplot as plt

############################################################
#NUMPY TUTORIAL 01(b)
############################################################
#Task: use numpy to load the ZnO.xye X-ray diffraction pattern and then
#plot to view the largest peak
#You will need (on top of 01a things): (i) set_xlim and set_ylim methods
#for axes; (ii) np.searchsorted; (iii) argmax method for numpy arrays.

#Load data here (as per 01a):

#Define a function plot_range() which as well as taking the xye data as an
#argument(s), takes a range of two x values and plots only between those
#values. Use it to plot all of the data and then use it to plot one of the
#peaks.
def fig_setup(figsize=(10, 10)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    return fig, ax

#def plot_range(data, xmin, xmax):


#Modify your plot_range function to find the minimum and maximum y values
#over the range you are plotting and scale the y axis appropriately

#Modify your plot_range function so that xmin and xmax are None by default
#and if xmin is None, then the x minimum is the first value of x and the
#maximum the last if xmax is None. Name this function plot_range2:

#def plot_range2(data, xmin=None, xmax=None):
#    if type(xmin) == type(None):


#Define a new function plot_max, which takes only data and a width as the
#argument, and plots over an x range of width with the largest peak in the
#pattern at the centre. Use the function with a width of 1.5 to plot the 
#largest peak.

#def plot_max(data, width=1.5):

