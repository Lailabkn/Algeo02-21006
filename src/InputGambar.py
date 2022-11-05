import cv2
import os
import glob

def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

files = ".\dataset"

for filename in glob.iglob(f'{files}/*'):
    image = load_images(filename)
print(image)