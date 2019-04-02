#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing useful directory
import os
import numpy as np
from skimage.io import imsave, imread,imshow
from glob import glob
import numpy as np
import getopt
import argparse
import json
import cv2
import matplotlib.pyplot as plt


# In[2]:


# getting images and mask path
path_image="/home/anant/data_science_practicum/p3/dataset/neurofinder.00.00.test/images"
#path_mask="/home/anant/data_science_practicum/p3/dataset/neurofinder.00.00.test/images"


# In[3]:


images = sorted(glob(path_image+'/*.tiff'))
#masks = sorted(glob(path_mask+'/*.tiff'))


# In[4]:


# Converting images and mask to numpy array
imgs=[]
i=0
for image in (images):
    image_mat = imread(image)
    imgs.append(image_mat)

images_np = np.array(imgs)


# # Double Thresholding

# #### This is  a high pass filter applied on the image to enhance the small details in the image which could be help us. As you can se in the image displayed below the filtered image has more details than the original image. 

# In[6]:


#double thresholding
def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.09):
    
    highThreshold = img.max() * highThresholdRatio;
    lowThreshold = highThreshold * lowThresholdRatio;
    
    M, N = img.shape
    res = np.zeros((M,N), dtype=np.int32)
    
    weak = np.int32(25)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    return (res, weak, strong)


# In[10]:


res,weak,strong=threshold(img=images_np[0])


# In[83]:


#after applying double thresholding
display(res, images_np[0],title1="double thresholding",title2="original")


# # Filtering for removal of noise

# #### It will help in removal of noise from the image. I tried median filtering and gaussian filtering. So in our case i think gaussian blur will work better. The median filter totally remove the noise but noise can also be the relevant information in our case on the other hand the gaussian filter it doesnot totally remove the nosise but the lessen its intensity which is still better the original image.

# In[84]:


i= np.float32(res)


# In[85]:


median=cv2.medianBlur(i,3)
gaus=cv2.GaussianBlur(i,(5,5),0)


# In[86]:


display(median,gaus)


# # Display function 

# In[87]:


def display(a, b, title1 = "median filtering", title2 = "gaussian"):
    plt.subplot(121), plt.imshow(a), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(b), plt.title(title2)
    plt.xticks([]), plt.yticks([])
    #plt.subplot(123), plt.imshow(c,cmap='gray'), plt.title(title3)
    #plt.xticks([]), plt.yticks([])
    plt.show()

