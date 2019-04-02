import json
import matplotlib.pyplot as plt
from numpy import array, zeros
from cv2 import imread,imwrite
from glob import glob
import scipy.misc
import os
from os import listdir
import cv2
import PIL

#Get the names of all the folders

extractpathTrain = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\extractedZipTrain"

files = [f for f in os.listdir(extractpathTrain)]
extractedFilesTrain = []
for file in files:
    print(file)
    if "zip" not in file:
        extractedFilesTrain.append(file)

print(extractedFilesTrain)

#Create Mask

extractPathTrain = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\extractedZipTrain"
for fileName in extractedFilesTrain:
    print(fileName)
    # load the images
    files = sorted(glob(extractPathTrain + '\\' + fileName + '\\' +'images\\*.tiff'))
    imgs = array([plt.imread(f) for f in files])
    dims = imgs.shape[1:]
    with open(extractPathTrain + '\\' + fileName + '\\' + 'regions/regions.json') as f:
        regions = json.load(f)
    masks = array([tomask(s['coordinates']) for s in regions])
    # show the outputs
    plt.figure()
    #plt.subplot(1, 2, 1)
    #plt.imshow(imgs.sum(axis=0), cmap='gray')
    plt.subplot(1, 2, 2)
    plt.imshow(masks.sum(axis=0), cmap='gray')

    savePath = "D:\\Sushanth\\UGA Notes\\Sem2-DSP,DM,DCS\\DSP\\Projects\\Project 3\\project3\\trainingMask"
    plt.imsave(savePath+ '\\' + fileName + '.jpg' , masks.sum(axis=0))
    #plt.show()

    
    
    
   def tomask(coords):
    for cord in coords:
        mask = zeros(dims)
        mask[cord[0]][cord[1]] = 1
        return mask
