import json
import thunder as td
from extraction import NMF
import os

# change the directory to the test directory 
os.chdir('e:/project3/test/')

datasets = ['00.00.test','00.01.test']
# datasets = ['00.00.test','00.01.test','01.00.test','01.01.test','02.00.test','02.01.test','03.00.test','04.00.test','04.01.test']

submission = []

for dataset in datasets:
    print('processing dataset: %s' % dataset)
    print('loading')
    path = 'neurofinder.' + dataset
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