import cv2
import numpy as np 

## Resizing images
# img = cv2.imread('Resources/lena.png')
# print(img.shape) #(512, 512, 3)
# img_resize = cv2.resize(img, (300, 200))
# print(img_resize.shape) #(200, 300, 3)
# cv2.imshow('Output', img)
# cv2.imshow('Resize Output', img_resize)
# cv2.waitKey(0)


### Croping Image
img = cv2.imread('Resources/lambo.png')
crop_img = img[0:200,200:500]
cv2.imshow('Output', img)
cv2.imshow('Crop_Output', crop_img)
cv2.waitKey(0)