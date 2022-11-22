#FILE TEST UNTUK MEMERIKSA MEAN

from InputGambar import *
import numpy as np
import cv2
from PIL import Image


S = np.array(load_images_folder2('.\dataset')) # load images from folder (bukan flaten matrix)
mean = np.mean(S, axis=0) # Calculate mean of images
mean_resize = cv2.resize(mean, (256,256))
mean_img = Image.fromarray(mean_resize)
mean_img.show() # Show mean image