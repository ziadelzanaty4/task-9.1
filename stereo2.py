import cv2
import numpy as np


fx = 6338.47
baseline = 171.548/ 10.0   # convert mm to cm
doffs = 479.489              

left_img = cv2.imread('img1/im0.png', 0)
right_img = cv2.imread('img1/im1.png', 0)

matcher = cv2.StereoBM_create(numDisparities=400, blockSize=15)


disparity = matcher.compute(left_img, right_img)

# StereoBM gives back the disparity scaled by 16, so we fix that here
disparity = disparity.astype(np.float32) / 16.0

disp_view = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)
disp_view = np.uint8(disp_view)

cv2.imwrite('img1/disparity_gray.png', disp_view)
disp_color = cv2.applyColorMap(disp_view, cv2.COLORMAP_JET)
cv2.imwrite('img1/disparity_color.png', disp_color)

def get_depth(disp_map, x, y, fx, baseline, doffs):
    d = disp_map[y, x]
    if d <= 0:
        return None
    return (fx * baseline) / (d + doffs)

x = 1450
y = 900
depth = get_depth(disparity, x, y, fx, baseline, doffs)

if depth is not None:
    print(f"Depth at pixel ({x}, {y}): {depth:.2f} cm")
else:
    print(f"No valid disparity at pixel ({x}, {y}), try another point")

left_view = cv2.resize(left_img, (700, 700))
gray_view = cv2.resize(disp_view, (700, 700))
color_view = cv2.resize(disp_color, (700, 700))

cv2.imshow('Left Image', left_view)
cv2.imshow('Disparity (gray)', gray_view)
cv2.imshow('Disparity (color)', color_view)
cv2.waitKey(0)
cv2.destroyAllWindows()    