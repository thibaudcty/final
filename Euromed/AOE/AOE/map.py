

import pygame
import numpy

##VARIABLES A IMPORTER

from Euromed.AOE.AOE.definitions import MAP_SIZE



def noise(seed,x,y) :
    x = (x >> seed//2) ^ x
    y = (y >> seed//2) ^ y
    noisedX = (x * (x * x * 60493 + 19990303) + 1376312589) & 0x7fffffff
    noisedY = (y * (y * y * 60493 + 19990303) + 1376312589) & 0x7fffffff
    return 1.0 - (noisedX / 1073741824.0)


def randomMap() :
    from scipy.ndimage.interpolation import zoom

    arr = numpy.random.uniform(size=(4,4))
    arr = zoom(arr, MAP_SIZE/2)
    arr = arr > 0.8

    arr = numpy.where(arr, 'water', 'grass')
    return arr
