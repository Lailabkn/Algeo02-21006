import os
import cv2
import numpy as np
from eigen import *
# from PIL import Image
# from EigenVector import EigenVector
# from Operation import *
from InputGambar import *
from Main import *


tes = '.\dataset\Zendaya.jpg'
TestFace = np.array(load_images_file(tes))
selisihface = np.array(abs(TestFace - mean))
covarianface = np.array(np.cov(selisihface))
eigenvek = np.array(eigVec(covarianface))
eigenfacetest = np.array(np.dot(eigenvek, selisihface))
print(eigenfacetest)