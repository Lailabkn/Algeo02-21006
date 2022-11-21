# import os
from InputGambar import *
import numpy as np
from PIL import Image
from eigen import *
from Operation import *

# DATASET
S = np.array(load_images_folder(".\dataset"))
H = np.transpose(S)
mean = np.mean(S, axis=0) # Calculate mean of images
sel = np.array(abs(S - mean))# Calculate difference between images and mean
trans = np.transpose(sel)
cov = np.array(np.matmul(sel, trans))# Calculate covariance of difference
vektoreigen = np.array(eigVec(cov)) # Calculate eigen vector of covariance
eigenfaces = np.array(np.matmul(vektoreigen, sel)) # Calculate eigen face

# TEST(Inputan)
tes = '.\dataset\Alexandra Daddario.jpg'
TestFace = np.array(load_images_file(tes))
selisihface = np.array(abs(TestFace - mean))
eigenfacestest = np.array(np.matmul(eigenfaces, selisihface))
# print(selisihface.shape)
print(eigenfacestest)
# print(TestFace.shape)
# print(S.shape)
# print(J)
# print(H.shape)
# print(sel)
# print(mean.shape)
# print(cov)
# print(vektoreigen.shape)
# print(eigenfaces)
# print(eigenfaces.shape)
# print(sel.shape)

# cv2.imshow("mean",mean)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
