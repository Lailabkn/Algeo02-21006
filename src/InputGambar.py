import cv2
import os
import numpy as np
from faceallig import *

# LOAD FOLDER
def list_files(directory):
    list_of_files = [] # list of files
    for folder, direct, file in os.walk(directory): 
        for filename in file: # for each file in folder
            list_of_files.append(os.path.join(folder, filename)) # add file to list
    return list_of_files

# WITH RAVEL(FLATTEN  IMG)-> matrix
def load_images_folder(folder):
    images = []
    for file in list_files(folder):
        images.append(load_images_file(file))
    return images

# LOAD IMAGE
def load_images_file(image):
    img = faceAlignment(cv2.resize(cv2.imread(image, cv2.IMREAD_GRAYSCALE), (256, 256))) # resize image ke 256 x 256, convert to grayscale
    img = img.ravel() # flatten image
    img = np.array(img) # convert to numpy array
    return img

# WITHOUT RAVEL(FLATTEN IMG) -> list of matrix
def load_images_folder2(folder):
    images = []
    for file in list_files(folder):
        images.append(load_images_file2(file))
    return images

# NORMALIZE
def load_images_file2(image):
    img = cv2.resize(cv2.imread(image, cv2.IMREAD_GRAYSCALE), (256, 256)) # resize image ke 256 x 256, convert to grayscale
    return img

# RESIZE IMAGE
def resize_images(images, size): 
    resized_images = []
    for image in images:
        resized_images.append(cv2.resize(image, size)) # resize image
    return resized_images