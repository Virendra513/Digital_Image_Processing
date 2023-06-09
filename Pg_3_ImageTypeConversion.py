# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 23:39:18 2023

@author: virendra Singh Kaira (22-27-05)
"""
#Reading of images and conversion btw unit8 and float64


from skimage import io
img_2=io.imread("E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png",as_gray=False)
print(img_2.shape)


img_3=io.imread("E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png")

from skimage import img_as_ubyte,img_as_float
img_3_float=img_as_float(img_3)

import numpy as np
img_3_numpy_float=img_3.astype(np.float)

img_3_float_to_uint8=img_as_ubyte(img_3_float)

#io.imshow('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png')
#**********************

import cv2



grey_img=cv2.imread('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png',0)
color_img=cv2.imread('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png',1)
cv2.imshow('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png',grey_img)
cv2.imshow('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png',color_img)
cv2.waitkey(0)
cv2.destroyAllWindows()

