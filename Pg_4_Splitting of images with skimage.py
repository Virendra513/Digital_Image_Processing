# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:53:05 2023

@author: virendra Singh Kaira (22-27-05)
"""
# Splitting of images with skimage 
from skimage import io
img=io.imread('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png')
print(img.shape)

from skimage import img_as_float
img2=img_as_float(img)
B = img2[:,:,0]
G = img2[:,:,1]
R = img2[:,:,2]

io.imshow(B)
io.imshow(G)
io.imshow(R)

# Splitting of images with computer vision
import cv2
img3=cv2.imread('E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png')
img4=cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
b,g,r=cv2.split(img3)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
cv2.waitKey(0)
cv2.destroyAllWindows()

