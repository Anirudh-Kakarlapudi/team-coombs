import os
import argparse
from src.unet import UNet
from src.nmf import model_implementaiton

# creating the parser
parser = argparse.ArgumentParser(description='Trains the model and outputs predictions.')

#adding agrument to the parser
parser.add_argument('--model', type=str, choices=['unet','nmf'], 
    default='unet', help = 'model for neuron finding')

#choose the model
args = parser.parse_args()
model = args.model

if model == 'unet':
    UNet(model)
elif model == 'nmf':
    model_implementaiton()

