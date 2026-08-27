import cv2
import numpy as np
import sys

def gray_world_white_balance(img):
    img = img.astype(np.float32)
    b, g, r = cv2.split(img)
    b_avg, g_avg, r_avg = np.mean(b), np.mean(g), np.mean(r)
    k = (b_avg + g_avg + r_avg) / 3
    b = np.clip(b * (k / b_avg), 0, 255)
    g = np.clip(g * (k / g_avg), 0, 255)
    r = np.clip(r * (k / r_avg), 0, 255)
    return cv2.merge([b, g, r]).astype(np.uint8)