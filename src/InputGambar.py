import cv2
import os
# from align_faces import align
import numpy as np
# from cobaaffh import *
from faceallig import *

def list_files(directory):
    list_of_files = []
    for folder, direct, file in os.walk(directory):
        for filename in file:
            list_of_files.append(os.path.join(folder, filename))
    return list_of_files

def load_images_folder(folder):
    images = []
    for file in list_files(folder):
        images.append(load_images_file(file))
    return images

def load_images_folder2(folder):
    images = []
    for file in list_files(folder):
        images.append(load_images_file2(file))
    return images

def load_images_file2(image):
    img = cv2.resize(cv2.imread(image, cv2.IMREAD_GRAYSCALE), (256, 256))
    return img

def load_images_file(image):
    img = faceAlignment(cv2.resize(cv2.imread(image, cv2.IMREAD_GRAYSCALE), (256, 256)))
    img = img.ravel()
    img = np.array(img)
    return img

def resize_images(images, size):
    resized_images = []
    for image in images:
        resized_images.append(cv2.resize(image, size))
    return resized_images