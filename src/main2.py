from InputGambar import *
import numpy as np
from PIL import Image
from eigen import *
import cv2
import timeit

# START TIMER
start = timeit.default_timer()

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

eigenfaces = np.array(np.matmul(eigenvector.T, sel)) # Calculate eigen face
weight = np.array(np.matmul(eigenfaces, sel.T))


# TEST(INPUT)
test = '.\Zendaya13_1806.jpg'
TestFace = np.array(load_images_file(test))
selisihface = np.array(abs(TestFace - mean))
selisihfaces = selisihface.reshape(65536, 1)
weighttest = np.array(np.matmul(eigenfaces, selisihfaces))

a = np.array(np.square(weight - weighttest))
b = np.sum(a, axis=0)
euclidean = np.sqrt(b)

# MENGELUARKAN INDEX GAMBAR YANG SAMA(DISTANCE TERKECIL)
minus = min(euclidean)
def searchIndex (L, minus):
    for i in range (len(L)):
        if (L[i] == minus):
            return i+1
index = searchIndex(euclidean, minus)
print(index)

# MENGELUARKAN GAMBAR YANG SAMA (RGB)
for i in range(len(S)):
    if i == index-1:
        S = S[i].reshape(256, 256)
        S_rgb = cv2.cvtColor(S, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(S_rgb)
        image.show()

# STOP TIMER
stop = timeit.default_timer()
total = stop - start
mins, secs = divmod(total, 60)
hours, mins = divmod(mins, 60)

# MENGELUARKAN WAKTU EKSEKUSI
print("Time: %d:%02d:%02d" % (hours, mins, secs))