# small script meant to display square images from .npy file

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


path = input("What is the name of the .npy file in './data/' to display? (Exclude '.npy')\n> ")
path = 'data/' + path + '.npy'
# path = "data/upside_down_faces.npy" # manually provide path for now
try:
    data = np.load(path)
except:
    input("Error locating/finding specified file.\nPress Enter to quit.")
    exit()

# assumes data shape is (number of images, pixel in image)
(numImages, imgVecLength) = data.shape

# check that images are actually square
root = np.sqrt(imgVecLength)
if int(root + .5) ** 2 != imgVecLength:
    input("Images aren't square.\nPress Enter to quit.")
    exit()
else:
    imgSideLength = int(root)

# resize image vector to square shape
squareData = data.reshape((numImages, imgSideLength, imgSideLength))

# display images
idx0 = 0
img = plt.imshow(squareData[idx0], cmap='gray_r', vmin=0, vmax=255)
img.axes.xaxis.set_visible(False)
img.axes.yaxis.set_visible(False)

# position of slider axis
axidx = plt.axes([0.2, 0.02, 0.7, 0.03])
slidx = Slider(axidx, 'Image number', 0, numImages-1, valinit=idx0, valfmt='%d')

def update(val):
    idx = slidx.val
    img.set_data(squareData[int(idx)])
slidx.on_changed(update)

plt.show()