# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:16:34 2023

@author: viren
"""

""" Reading Images into Python
Scikit-image: pip install scikit=image
opencv: pip install opencv-python

Pillow: PIL - does not import images as numpy array.
You can convert using  numpy.asarray(img)
"""
from skimage import io,img_as_float,img_as_ubyte

img=io.imread("E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png")
print(img.shape)
img_float=img_as_float(img)
img2=img_as_ubyte(img_float)


import cv2
img_cv2=cv2.imread("E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png")

#BGR instead of RGB

grey_img=cv2.imread("E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png",0)
color_img=cv2.imread("E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png",1)

img_opencv= cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)