import os
from Matrix import *
from InputGambar import *

S = resize_images(load_images(".\dataset"), (256, 256))
displayListMatrix(S)