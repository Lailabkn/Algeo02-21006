from InputGambar import *
import numpy as np
from PIL import Image
from eigen import *

# DATASET
S = np.array(load_images_folder(".\dataset"))
H = np.transpose(S)
mean = np.mean(S, axis=0) # Calculate mean of images
meanimage = mean.reshape(256, 256)

sel = np.array(abs(S - mean))# Calculate difference between images and mean
trans = np.transpose(sel)
cov = np.array(np.matmul(sel, trans))# Calculate covariance of difference
cov = cov/len(cov)

eigenvector = np.array(eigVec(cov)) # Calculate eigen vector of covariance


for i in range(len(eigenvector)):
    norm = Normalize(eigenvector[i])
    eigenvector[i] = eigenvector[i]/norm

# for i in range(len(eigenvector)):
#     eigenface = np.array(np.matmul(eigenvector[i], sel.T[i])) # Calculate eigen face
# print(eigenface.shape)

eigenfaces = np.array(np.matmul(eigenvector.T, sel)) # Calculate eigen face
# print(eigenfaces.shape)
weight = np.array(np.matmul(eigenfaces, sel.T))


test = '.\Zendaya13_1806.jpg'
TestFace = np.array(load_images_file(test))
selisihface = np.array(abs(TestFace - mean))
selisihfaces = selisihface.reshape(65536, 1)
weighttest = np.array(np.matmul(eigenfaces, selisihfaces))

a = np.array(np.square(weight - weighttest))
b = np.sum(a, axis=0)
euclidean = np.sqrt(b)
# print(euclidean)

minus = min(euclidean)
def searchIndex (L, minus):
    for i in range (len(L)):
        if (L[i] == minus):
            return i+1

index = searchIndex(euclidean, minus)
print(index)
# print(min(euclidean))
for i in range(len(S)):
    if i == index-1:
        S = S[i].reshape(256, 256)
        image = Image.fromarray(S)
        image.show()