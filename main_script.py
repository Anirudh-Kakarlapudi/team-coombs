#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import argparse
from src.models.unet import UNet
from src.models.thunder import thunder

# creating the parser
parser = argparse.ArgumentParser(description='Trains the model and outputs predictions.')

#adding agrument to the parser
parser.add_argument('--model', type=str, choices=['unet','thunder'], 
    default='unet', help = 'model for neuron finding')

#choose the model
args = parser.parse_args()
model = args.model

if model == 'unet':
    UNet(model)
elif model == 'thunder':
    thunder(model)

