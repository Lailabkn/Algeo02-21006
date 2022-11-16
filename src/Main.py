import os
# from Matrix import *
from InputGambar import *
import numpy as np
from PIL import Image
from eigen import *
from EigenVector import *
from EigenFace import *
from Operation import *

S = np.array(resize_images(load_images_folder(".\dataset"), (256, 256))) # Load images from folder
mean = np.mean(S, axis=0) # Calculate mean of images

sel = np.array(selisih(S,mean)) # Calculate difference between images and mean

cov = np.array(covarian(sel)) # Calculate covariance of difference

eigvec = np.array(EigenVectorList(cov)) # Calculate eigen vector of covariance

for i in range(0, len(eigvec), 1): # Calculate eigen face
    eigvec[i] = np.dot(eigvec[i], sel[i]) 

print(eigvec)