
#importing useful directory
from os import listdir
import numpy as np
from glob import glob
import numpy as np
import getopt
import argparse
import json
import cv2
import json
import thunder as td
from extraction import NMF
import os

def read_dir(path):
    onlyfiles = [f for f in listdir(path)]
    return onlyfiles

def appending_path(onlyfiles,path):
    image_path=list()
    for i in (onlyfiles):
        i=path+i+"/images"
        image_path.append(i)
    return image_path

def getting_image(image_path):
    image_list=list()
    for i in (image_path):
        image_list.append(sorted([os.path.join(i,file)
                 for file in os.listdir(i) if file.endswith('.tiff')]))
    return image_list

def image_to_array(image_list):
    for j in range(0,len(image_list)):
        img = [cv2.imread(i, cv2.IMREAD_UNCHANGED) for i in image_list[j]]
    return img

def applying_thresholding(img):    
    img_res=[]
    for i in img:
        res, weak, strong=threshold(i) 
        img_res.append(filtering_noise(res))
    return img_res

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

# applying gausian filtering in the code
def filtering_noise(res):
    i= np.float32(res)
    #median=cv2.medianBlur(i,3)
    gaus=cv2.GaussianBlur(i,(5,5),0)
    return gaus

def model_thunder(img_res):
    print("the model_creation")
    submission=[]
    algorithm = NMF(k=5, percentile=99, max_iter=10, overlap=0.1)
    model = algorithm.fit(img_res, chunk_size=(50,50), padding=(25,25))
    merged = model.merge(0.1)
    print('found %g regions' % merged.regions.count)
    regions = [{'coordinates': region.coordinates.tolist()} for region in merged.regions]
    result = {'dataset': onlyfiles, 'regions': regions}
    submission.append(result)
    print('writing results')
    with open('submission4.json', 'w') as f:
        f.write(json.dumps(submission))
    return

def main():
    
    #creating parser
    parser = argparse.ArgumentParser(
        description=('Trains the model and outputs predictions.'),
        add_help='How to use', prog='model.py <args>')

    # Required arguments
    parser.add_argument("--data_path", required=True,
                        help=("Provide the path to the data folder"))
    #input to the path of the dataset
    args=vars(parser.parse_args())                     #input("enter the path of dataset:")
    path=args['data_path']
    print(path)
    # getting the directory inside the dataset
    onlyfiles=read_dir(path)
    # appending directory name in dataset with the path
    image_path=appending_path(onlyfiles,path)
    # getting all images from the path
    image_list=getting_image(image_path)
    # storing image in numpy array
    img=image_to_array(image_list)
    # preprocessing
    img_res=applying_thresholding(img)
    # applying thunder and saving the json file
    model_thunder(img_res)
    print("Task completed")
    
    
if __name__ == '__main__':
    main()

