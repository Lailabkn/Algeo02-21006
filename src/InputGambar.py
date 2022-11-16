import cv2
import os
# from Matrix import *
import numpy as np

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

def load_images_file(image):
    img = cv2.resize(cv2.imread(image, cv2.IMREAD_GRAYSCALE), (256, 256))
    return img

def resize_images(images, size):
    resized_images = []
    for image in images:
        resized_images.append(cv2.resize(image, size))
    return resized_images