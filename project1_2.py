# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:01:09 2023

@author: bchan
"""


# Data structures and analysis
import numpy as np

# Visualization
# import matplotlib.pyplot as plt
# import pyvista as pv


# This line reads information from the file into a 3D numpy array called img.
# The dimensions of the entire volume are stated below and used in reshape function call.
nz = 111
ny = 100
nx = 100

img = np.fromfile('fracture.raw', dtype=np.uint8)
img = img.reshape(nz,ny,nx)





#%%
####################################
# Your image in 3D is a stack in z-direction of 2D images ((x,y) plane).  For every (x,y) coordinate
# there is a column of nz values in img and those that are belonging to fracture (0s) have certain height
# that is called an aperture.
# Create a function called 'create_aperture' that takes 3D img array as an input and returns aperture field a.

#####################################










        

#%%
#####################################
# Problem 3:
# Define a function called "aperture_statistics" 
# that computes and returns the Minimum, Maximum of any aperture field.
# Execute this function using above aperture field a.
####################################








#%%
####################################
# Problem 4:
# Define a function called "aperture_mean" 
# that calculates and returns the mechanical aperture (eq. 1 from paper in repo)
# Execute this function using above aperture field a.
###################################











#%%
####################################
# Problem 5:
# Define a function called "roughness_coeff" 
# that calculates and returns the roughness coefficient (eq. 2 from paper in repo)
# Execute this function using above aperture field a.
###################################









#%%
####################################
# Problem 6:
# Define a function called "tortuosity" 
# that calculates and returns the tortuosity (eq. 3 from paper in repo)
# Execute this function using above aperture field a.
###################################











#%%
####################################
# Problem 7:
# Define a function called "perm" that calculates and returns permeability k
# Refer to volumetric flux estimate using cubic formula (ref. Problem 2B.3c in BSL, see readme file)
# where 2*B is equal to mean aperture calculated in Problem 4.
# Further, compare volumetric flux to Darcy's law to calculate permeability k of the "parallel plate" fracture with the
# same aperture as the mean (calculated in Problem 4)

###################################













