# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:31:31 2023
Showing of Image Channels BGR 
@author: virendra Singh Kaira 
"""
from skimage import io
img=io.imread('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png')
print(img.shape)

from skimage import img_as_float
img2=img_as_float(img)

import numpy as np
img3=img.astype(np.float)

from skimage import img_as_ubyte
img_8= img_as_ubyte(img2)

io.imshow(img_8)

import cv2
grey_img= cv2.imread('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png',0)
color_img=cv2.imread('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png',1)
cv2.imshow('jjj',grey_img)
cv2.imshow('fff',color_img)
cv2.destroyAllWindows()
B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]

io.imshow(B)
io.imshow(G)
io.imshow(R)
