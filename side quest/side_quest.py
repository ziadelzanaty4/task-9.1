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


def apply_clahe(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge([l, a, b])
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

def correct_colors(img):
    wb = gray_world_white_balance(img)
    result = apply_clahe(wb)
    return result

if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv) > 1 else "input_image.png"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output_image.png"

    img = cv2.imread('side quest/input_image.png')
    corrected = correct_colors(img)

    stacked = np.hstack([img, corrected])
    cv2.imwrite('side quest/output_image.png', corrected)
    cv2.imwrite("side quest/comparison.png", stacked)