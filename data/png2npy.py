import numpy as np
import matplotlib.image as mpimg

def png2npy(path):
    im = mpimg.imread(path)
    bwim = np.sum(im, axis=2) / 3 # crude way to make black and white
    
    np.save(path[:-4] + '.npy', bwim.flatten())
    print("Saved as " + path[:-4] + '.npy')