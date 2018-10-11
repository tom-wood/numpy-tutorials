import numpy as np
import matplotlib.pyplot as plt

############################################################
#NUMPY TUTORIAL 04(a)
############################################################
#Task: load ZnO.xye and find all the peaks

#Load data here (as per 01a):
fpath = '/home/tomwood/Documents/Misc/numpy-tutorials/ZnO.xye'
data = np.loadtxt(fpath)

def fig_setup(figsize=(10, 10)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    return fig, ax

#Write a peak identification function, that looks through data and decides
#where the peaks are, returning their positions. You might find the
#rolling average function you wrote in tut03a useful (or you might not).
#You will have to decide what parameters to put in to your function (as a
#guide, I used 3 parameters other than data for my function---it may well
#be possible to do it with fewer than that).

#Write a function that plots the data with markers on all the peaks (as a
#check for the first function). You will need plt.text (or ax.text) or
#plt.vlines, depending on preference.

#Write another function (which could call the first), that finds the linear
#background-corrected areas under all the peaks and returns the positions
#and areas by order of area or x-position depending on an argument to the
#function.

#Write a final plotting function which plots the data and labels the peaks
#in order numerically (either by x position or by area; you'll need
#plt.text for this).
