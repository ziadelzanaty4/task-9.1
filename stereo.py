import cv2
import numpy as np


fx = 3979.911
baseline = 193.001 / 10.0   # convert mm to cm
doffs = 124.343              

left_img = cv2.imread('im0.png', 0)
right_img = cv2.imread('im1.png', 0)