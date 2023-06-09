# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:25:02 2023

@author:Virendra Singh Kaira(22-27-05)
"""
from skimage import io
import cv2
import glob


m_list=glob.glob("E:\DS_ACADEMIC\DS2\DIP\glob\*.*")
print(m_list)


file_list=[]

for file in m_list:
    print(file)
    a=cv2.imread(file)
    file_list.append(a)

from matplotlib import pyplot as plt
plt.imshow(file_list[0])

from skimage import img_as_float
floatimage=img_as_float(file_list[1])



#######################
img_number=1
for file in m_list:
     a=cv2.imread(file)
    
c=cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
cv2.imwrite("E:\DS_ACADEMIC\DS2\DIP\glob\glob_mod"+str(img_number)+"jpg",c)
img_number+=1
cv2.imshow("Color image",c)
cv2.waitkey(1000)
cv2.destroyAllWindows()