from os import listdir
import numpy as np
from glob import glob
import numpy as np
import getopt
import argparse
import json
#import cv2
import json
import thunder as td
from extraction import NMF
import os
import zipfile

def extract_zip_data(path):
        files = os.listdir(path)
        print(files)
        for file in files:
            print("Extracting "+file)
            filepath = path+ file
            print(filepath)
            zip_ref = zipfile.ZipFile(filepath, 'r')
            print(zip_ref)
            if file[-8:] == 'test.zip':
                zip_ref.extractall(get_test_path(path))
            else:
                zip_ref.extractall(get_train_path(path))
            zip_ref.close()
                  
def get_train_path(path):
        train=path+"data/train/"
        return train
    
def get_test_path(path):
        test=path+"data/test/"
        return test
    
def read_dir(path):
    #path= "/home/anant/data_science_practicum/p3/dataset/test/"
    onlyfiles = listdir(path)
    return onlyfiles

def model_implementaiton(datasets,path):
    submission = []
    for dataset in datasets:
        print(path)
        print('processing dataset: %s' % dataset)
        print('loading')
        temp_path = path+dataset
        print(temp_path)
        data = td.images.fromtif(temp_path + '/images', ext='tiff')
        print('analyzing')
        #algorithm = NMF(k=5, percentile=99, max_iter=50, overlap=0.1)
        algorithm = NMF(k=5, percentile=99, max_iter=10, overlap=0.1)
        model = algorithm.fit(data, chunk_size=(50,50), padding=(25,25))
        merged = model.merge(0.1)
        print('found %g regions' % merged.regions.count)
        regions = [{'coordinates': region.coordinates.tolist()} for region in merged.regions]
        result = {'dataset': dataset, 'regions': regions}
        submission.append(result)
    print('writing results')
    with open('submission.json', 'w') as f:
        f.write(json.dumps(submission))
        
def main():
    #creating parser
   
    parser = argparse.ArgumentParser(
        description=('Trains the model and outputs predictions.'),
        add_help='How to use', prog='model.py <args>')

    # Required arguments
    parser.add_argument("--data_path", required=True,
                        help=("Provide the path to the data folder"))
    #input to the path of the dataset
    args=vars(parser.parse_args())
    path=args['data_path']
    print(path)
    os.chdir(path)
    # unzipping the file
    if os.path.exists("data"):
            print('Data Folder is ready')
    else:
            print('hello')
            extract_zip_data(path)
    #extract_zip_data(path)
    # creating train folder
    #train_path=get_train_path(path)
    #creating test folder
    test_path=get_test_path(path)
    print(test_path)
    # getting the directory inside the dataset
    onlyfiles=read_dir(test_path)
    # applying thunder and saving the json file
    model_implementaiton(onlyfiles, test_path)
    print("Task completed")

if __name__ == '__main__':
    main()
