
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
    #path= "/home/anant/data_science_practicum/p3/dataset/test/"
    onlyfiles = [f for f in listdir(path)]
    return onlyfiles

def model_implementaiton(datasets,path):
    submission = []
    for dataset in datasets:
        print('processing dataset: %s' % dataset)
        print('loading')
        path = path+dataset
        data = td.images.fromtif(path + '/images', ext='tiff')
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
        with open('submission3.json', 'w') as f:
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
    args=vars(parser.parse_args())
    # getting the directory inside the dataset
    onlyfiles=read_dir(args['data_path'])
    # applying thunder and saving the json file
    model_implementaiton(onlyfiles,args['data_path'])
    print("Task completed")

if __name__ == '__main__':
    main()

