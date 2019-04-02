'''
This script converts the regions to masks
----------------------------------------
Authors:
Sushanth Kathirvelu
'''


import json
import matplotlib.pyplot as plt
from numpy import array, zeros
from glob import glob
import os
from Loader import Loader


dl = Loader()


def region_to_mask():
    '''
    function to create masks from the regions provided.
    It saves the mask image at data/training_masks
    '''

    for fileName in os.listdir(dl.get_train_path()):
        # load the images
        files = sorted(glob(dl.get_train_path() + '/' + fileName + '/' +
                            'images/*.tiff'))
        imgs = array([plt.imread(f) for f in files])
        dims = imgs.shape[1:]
        with open(extractPathTrain + '/' + fileName + '/' +
                  'regions/regions.json') as f:
            regions = json.load(f)
        masks = array([tomask(s['coordinates']) for s in regions])
        os.makedirs('../../data/training_masks')
        savePath = '../../data/training_masks/'
        plt.imsave(savePath + '/' + fileName + '.jpg', masks.sum(axis=0))


def tomask(coords):
    '''
    function to convert the region co-ordinates into mask array

    Args:
        co-ordinates of the regions
    Returns:
        Mask array.
    '''
    for cord in coords:
        mask = zeros(dims)
        mask[cord[0]][cord[1]] = 1
        return mask
