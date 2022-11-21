# from TestFace import*
from Main import*

# def euclidean_distance(x, y):
#   hasil = []
#   for i in range(len(y)):
#     hasil.append(np.linalg.norm(x-y[i]))
#   return hasil

tes = '.\dataset\Alexandra Daddario.jpg'
TestFace = np.array(load_images_file(tes))
selisihface = np.array(abs(TestFace - mean))
covarianface = np.array(np.cov(selisihface))
eigenvek = np.array(eigVec(covarianface))
eigenfacetest = np.array(np.dot(eigenvek, selisihface))

S = np.array(resize_images(load_images_folder(".\dataset"), (256, 256))) # Load images from folder
mean = np.mean(S, axis=0) # Calculate mean of images
sel = np.array(selisih(S,mean)) # Calculate difference between images and mean
cov = np.array(covarian(sel)) # Calculate covariance of difference
eigvec = np.array(EigenVectorList(cov)) # Calculate eigen vector of covariance
for i in range(0, len(eigvec), 1): # Calculate eigen face
    eigvec[i] = np.dot(eigvec[i], sel[i]) 

# print (euclidean_distance(eigenfacetest, eigvec))
# minus = 0
# ayey = 0 
# J = euclidean_distance(eigvec, eigenfacetest)
# if (i == 0) :
#   minus= J[i]
#   ayey = i
# else :
#   if (J[i] < minus):
#     minus = J[i]
#     ayey = i
#   print(ayey)

minus = 0
for i in range (len(eigvec)):
    dist = np.linalg.norm(eigenfacetest - eigvec[i])
    if (i == 0) :
        minus = dist
        ayey = i
    else :
        if (minus > dist) :
            minus = dist
            ayey = i
print(ayey)