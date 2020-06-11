# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:01:29 2020

@author: Ben
"""

from PIL import Image
import cv2
import os
import argparse
from glob import glob

path = os.getcwd()
parser = argparse.ArgumentParser()
parser.add_argument('input_dir', type=str, help='Input directory', nargs="?")
parser.add_argument('output_dir', type=str, help='Output directory', nargs="?")
args = parser.parse_args()
files = glob(os.path.join(args.input_dir, "*.*"))
for file in files:
    name = str.split(file,'\\')[-1]
    print(name)
    name = "inverse_" + name
    img = cv2.imread(file)
    dim=(1024,1024)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    final_img = 255-resized
    final_img = Image.fromarray(final_img)
    out = os.path.join(path,args.output_dir)
    out = os.path.join(out,name)
    final_img.save(out)
    name = ""
    out = ""
    
        