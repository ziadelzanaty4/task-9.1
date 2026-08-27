## 📷 Stereo Vision Depth Estimation Update

# 📸 1. Stereo Images

- I worked on a **Stereo Vision** project using a pair of left and right stereo images.
- The images were already rectified and grayscale, and I used image pairs from the **Middlebury Stereo Dataset**.
- Each dataset also provided the required calibration parameters for the depth calculations.

# 🔍 2. Disparity Map

- I used OpenCV `StereoBM` to calculate the disparity between the left and right images.
- I normalized the disparity map and saved the results as both a grayscale image and a color heatmap.
- I also noticed that disparity quality depends heavily on the amount of texture in the image, with flat areas potentially producing invalid or unreliable disparity values.

# 📏 3. Depth Estimation

- I used the disparity value at a selected pixel to estimate its real-world depth.
- The required calibration parameters were used, including the focal length (`fx`), baseline, and `doffs`.
- The depth was calculated using:

```text
depth = (fx * baseline) / (disparity + doffs)
```

- The baseline represents the physical distance between the two cameras, so it was converted from mm to cm to obtain the final depth in centimeters.

# ⚙️ 4. Important Implementation Details

- I found that `StereoBM.compute()` returns disparity in a fixed-point format, so the raw output needs to be divided by 16 before being used.
- I also made sure not to resize the images before calculating disparity, since resizing changes the pixel scale and makes the original `fx` calibration value inconsistent with the image.
- Resizing was only performed after the calculations for display purposes.

# 🧪 5. Improvements & Testing

- I experimented with different `StereoBM` settings, including texture, uniqueness, and speckle filtering.
- These adjustments helped reduce noise and produced a cleaner disparity map compared to the default settings.
- For reliable depth estimation, I also learned that the selected pixel should belong to a textured object rather than a flat, low-texture area.
