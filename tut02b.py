import numpy as np
import matplotlib.pyplot as plt

############################################################
#NUMPY TUTORIAL 02(b)
############################################################
#Task: load ZnO.xye and write a function to calculate a local linear
#background fit and then use it to find a corrected area under a peak
#You might find np.polyfit useful.

#Load data here (as per 01a):
fpath = '/home/tomwood/Documents/Misc/numpy-tutorials/ZnO.xye'
data = np.loadtxt(fpath)

#Plot the x (2 theta) vs y (intensity) here:
def fig_setup(figsize=(10, 10)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    return fig, ax

#Make a new function akin to plot_max() from 01b, which: (i) takes data as
#an argument; (ii) takes xmin/xmax arguments; (iii) within data[xmin:xmax]
#finds the maximum peak and cuts data down to a certain width either side of
#it; (iv) cuts the peak out of the data, such that only the background
#either side remains (use a peak_width argument for that); (v) return 
#trimmed down data.
#def get_max_bgd(data, xmin=None, xmax=None, width=1.5, peak_width=1.0):

#Also, write a function that takes the original data and the new trimmed
#data and overlays the latter on the former (as a check that the first
#function worked). Make sure that it only plots between the xmin and xmax
#of the trimmed down data.

#Write a function that calls the first function to get trimmed down 
#background data, fits a linear background to it and then returns said fit.
#Use the plot function to check the linear fit against the data.

#Finally, define a function that finds the area under a peak, once the 
#linear background has been corrected for. Does it differ significantly
#from your original area? Should it?
