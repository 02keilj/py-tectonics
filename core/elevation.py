from scipy.spatial import cKDTree
import numpy as np

def rasterise_plates(points, width, height):
    tree = cKDTree(points)
    yy, xx = np.mgrid[0:height, 0:width]
    pixels = np.c_[xx.ravel(), yy.ravel()]
    _, indices = tree.query(pixels)
    plate_grid = indices.reshape(height, width)
    return plate_grid