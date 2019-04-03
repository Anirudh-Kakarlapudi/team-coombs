"""
This is a script to convert the predictions to regions
-------------------------------------
Author: Sushanth Kathirvelu
"""
import json
import matplotlib.pyplot as plt
from numpy import array, zeros
import numpy as np
from scipy.misc import imread, imsave
from PIL import Image

mask = Image.open('../../training_masks/neurofinder.00.00.png')
mask = array(mask)
coordinates = []
print(mask.shape)
print(np.unique(mask))

for x in range(mask.shape[0]):

    for y in range(mask.shape[1]):

        #print(mask[x][y])
        if mask[x , y] !=  0:
            #print(mask[x, y])
            coordinates.append([x, y])

imsave('../../predictions/neurofinder.00.00.png', coordinates)
