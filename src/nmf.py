"""
Script to run the NMF model
This implementation is based on the implementation from
https://gist.github.com/freeman-lab/330183fdb0ea7f4103deddc9fae18113
--------------------------------
Authors:
Anirudh Kakarlapudi and Anant Tripathi
"""

import json
import thunder as td
from extraction import NMF
import os
from Loader import Loader

# Calling a dataloader class
dl = Loader()


def read_dir(path):
    '''
    Function to read the files in the directory

    Args:
        path: path of directory from which name of files should be returned.
    Returns:
    list of files in a directory
    '''
    onlyfiles = os.listdir(path)
    return onlyfiles


def model_implementaiton():
    '''
    Function to implement NMF on the data and Generate submissions.json file
    with all predicted regions.
    '''
    # Getting all the test files in the directory
    datsets = read_dir(d1.get_test_path)
    submission = []
    # Iterating over all the files to get regions.
    for dataset in datasets:
        print('processing dataset: %s' % dataset)
        print('loading')
        temp_path = dl.testpath + dataset
        print(temp_path)
        data = td.images.fromtif(temp_path + '/images', ext='tiff')
        print('analyzing')
        algorithm = NMF(k=10, percentile=98, max_iter=50, overlap=0.1)
        model = algorithm.fit(data, chunk_size=(50, 50), padding=(25, 25))
        merged = model.merge(0.1)
        print('found %g regions' % merged.regions.count)
        regions = [{'coordinates': region.coordinates.tolist()} for
                   region in merged.regions]
        result = {'dataset': dataset, 'regions': regions}
        submission.append(result)
    # Writing into a json file.
    print('writing results')
    with open('submission.json', 'w') as f:
        f.write(json.dumps(submission))
    dl.remove_all_files()
