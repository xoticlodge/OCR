# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:22:04 2022

@author: Jacky
"""

import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'C:\\Users\\Jacky\\Pictures\\Camera Roll\\WIN_20220302_10_33_29_Pro.jpg'
IMAGE_PATH2 = 'C:\\Users\\Jacky\\Pictures\\Scans\\Scan_20210512_2.png'
reader = easyocr.Reader(['en'], gpu = False)
result = reader.readtext(IMAGE_PATH)
result2 = reader.readtext(IMAGE_PATH2)

result
result2[1]#store as an array if multiple text

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(IMAGE_PATH)
img = cv2.rectangle(img, top_left, bottom_right,(0,255,0),5)
#creates a rectangle within the read text,color of rectangle ,outline thickness 
img = cv2.putText(img,text, top_left, font, .5, (255,255,255),2,cv2.LINE_AA)
#pass imagine and text, position the text, fontsize, text color, font size 
plt.imshow(img)#visualize
plt.show()#show image

img2 = cv2.imread(IMAGE_PATH2)
for detection in result2:
    top_left2 = tuple([int(val) for val in detection[0][0]])
    bottom_right2 = tuple([int(val) for val in detection[0][2]])
    text2 = detection[1]
    font2 = cv2.FONT_HERSHEY_SIMPLEX
    img2 = cv2.rectangle(img2, top_left2, bottom_right2,(0,255,0),10)
    img2 = cv2.putText(img2, text2, top_left2, font2, 2, (255, 0, 0),2,cv2.LINE_AA)
    
plt.figure(figsize =(10,10))#image size
plt.imshow(img2)
plt.show()