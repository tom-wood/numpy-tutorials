import numpy as np
import matplotlib.pyplot as plt

############################################################
#NUMPY TUTORIAL 01(a)
############################################################
#Task: use numpy to load the ZnO.xye X-ray diffraction pattern and then
#plot to view it
#You will need: (i) np.loadtxt or np.genfromtxt; (ii) plt.plot;
#(iii) axes methods set_xlabel/set_ylabel and figure method tight_layout;
#(iv) np.linspace; (v) np.sqrt.

#Load data here:

#Plot the x (2 theta) vs y (intensity) here:
#I have defined a fig_setup function for you, which should get you
#started. Make sure you label the axes and look up how to use
#tight_layout. If your code runs successfully you may need to use
#plt.show() to display the plot.
def fig_setup(figsize=(10, 10)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    return fig, ax

#fig, ax = fig_setup()

#Plot the y data vs the e (error on y) data here (make sure it's a 
#scatter plot):
#fig, ax = fig_setup()

#Now plot the same y vs e data as a scatter plot, but this time plot a 
#smooth line through the data (1000 points is enough to make it look
#smooth). You'll need the max() and min() methods for numpy arrays.
#Why does e = squareroot(y)?

