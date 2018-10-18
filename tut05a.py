import numpy as np
import matplotlib.pyplot as plt

############################################################
#NUMPY TUTORIAL 05(a)
############################################################
#Task: load ZnO.xye and fit all the peaks

#Load data here (as per 01a):
fpath = '/home/tomwood/Documents/Misc/numpy-tutorials/ZnO.xye'
data = np.loadtxt(fpath)

def fig_setup(figsize=(10, 10)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    return fig, ax

#Tasks: (i) Write a function that takes some x data and other parameters
#(specifically: amplitude [a], centre [b] and full-width-half-maximum) and 
#returns a Gaussian function. Plot that function with the following values:
#(a, b, fwhm) = (1, 0, 1); (a, b, fwhm) = (2, 0, 1); (a, b, fwhm) = 
#(1, 1, 1); (a, b, fwhm) = (1, 0, 2) to check it works.


#Task (ii): Do the same as task (i) for a Lorentzian function.


#Task (iii): Find the largest peak. Write a function to estimate the
#amplitude, x-position and FWHM. Plot a Gaussian and Lorentzian with those
#estimates and plot the difference between the data and the fit below. The
#estimates will serve as starting guesses for your fitting function below,
#so don't worry if they're not the best fit---the idea is to make sure
#you get the right local minimum.


#Task (iv): Redo task (iii) but account for a local linear background.
#Write a function to calculate the sum of the squares of the residuals.


#Task (v): Using your sum of squares function, write a function that will
#fit the largest peak to either a Gaussian or a Lorentzian and return the
#best fits for a, b and fwhm. Use these to establish whether the peak is
#more Gaussian or more Lorentzian in character. Plot the fits to check that
#the code is working as intended. You may find it useful to import the
#minimize function from scipy.optimize.
