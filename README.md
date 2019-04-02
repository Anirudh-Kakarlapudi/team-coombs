# Neuron Finding
This can best be described as object-finding or image segmentation, where the goal is to design a model whose output is the coordinates to regions of interest in an image. There’s no discrete label; rather, the model needs to learn segments in a continuous two-dimensional plane; relevant information to learning these segments, however, may be strewn over a third dimension of time. This makes for a very high-dimensional, large-scale problem: the data are height-by-width-by-time, and the model needs to learn a height-by-width mapping of pixels, where each pixel is either part of a neuron, or isn’t. Each folder of training and testing images is a single plane, and the images are numbered according to their temporal ordering. The neurons in the images will “flicker” on and off, as calcium (Ca 2+ ) is added, activating the action potential gates. You’ll have to use this information in order to locate the neurons and segment them out from the surrounding image.

# Approach

* NMF to get neuron region coordinates using Thunder-Extraction

### NMF Flow
* Use thunder library and import that in your code.
* Load the testing dataset.
* Create the algorithm with various parameters.
* Fit the model in our algorithm.
* Transform and merge the overlapping coordinates.
* Save the output in desired format

# Data
The datasets we used to train and test is provided by Dr. Shannon Quinn for the course CSCI 8360: Data Science Practicum.

There are total 9(test) Dataset which are being evaluated.

Training and Testing Dataset can also be found on below website: https://console.cloud.google.com/storage/browser/uga-dsp/project3/

# Prerequisits

### The project requires the following technologies to be installed.

* Instructions to download and install Python can be found here. https://www.python.org/
* Instructions to download and install Thunder and Thunder extraction can be found here https://github.com/thunder-project/thunder


# How to Run
[1] Download the repository 
 
[2] Run the script main_script.py

`$ python3 main_script.py `

This script will:

* Download the data in data/download folder
* It will extract the zip file in data/test or data/test depending on the type of file.
* It will run the model
* The result will be saved in the submission file
* finally it will remove the data from the folder

# Results



# Authors
* Haixing Dai (hd54134@uga.edu)
* Anirudh Kakarlapudi (kakmaurya@uga.edu)
* Sushanth Kathirvelu (sk33167@uga.edu)
* Anant Tripathi (at41132@uga.edu)

# Contribution
There are no specific guidlines for contibuting. If you see something that could be improved, send a pull request! If you think something should be done differently (or is just-plain-broken), please create an issue.

# Reference
[1] https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123

[2] http://neurofinder.codeneuro.org/

[3] https://en.wikipedia.org/wiki/Non-negative_matrix_factorization

[4] https://github.com/thunder-project/thunder-extraction

[5] https://github.com/thunder-project

# License
This Project is under the MIT License. For more details visit License file here: https://github.com/dsp-uga/team-coombs/blob/master/LICENSE
