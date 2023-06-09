# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:05:53 2023

@author: virendra Singh Kaira (22-27-05)
"""

##Gaussian Filtering
from skimage import io
img=io.imread("E:\DS_ACADEMIC\DS2\DIP\Lenna_(test_image).png")
from skimage import filters
from skimage import img_as_ubyte
img_8bit=img_as_ubyte(img)
gaussian_img=filters.gaussian(img_8bit,sigma=3)
gaussian_img_2=filters.gaussian(img_8bit,sigma=2)
io.imsave("E:\DS_ACADEMIC\DS2\DIP\gaussian_img_new.jpg",gaussian_img)


# Plot figure 
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(15,15))
ax1=fig.add_subplot(1,3,1)
ax1.imshow(img)
ax1.title.set_text('Orginal File')

fig=plt.figure(figsize=(15,15))
ax1=fig.add_subplot(1,3,2)
ax1.imshow(gaussian_img_2)
ax1.title.set_text('2 Sigma')


fig=plt.figure(figsize=(15,15))
ax1=fig.add_subplot(1,3,3)
ax1.imshow(gaussian_img)
ax1.title.set_text(' 3 Sigma')