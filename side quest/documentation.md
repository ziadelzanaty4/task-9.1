# Color Correction — Side Quest 2

## Problem

The provided image has a strong teal/cyan color cast, typical of underwater
photography. Water absorbs red wavelengths first, so the red channel is
heavily attenuated compared to green and blue, leaving the whole image
looking green-blue instead of showing natural colors.

## Technique Used

**1. Gray World White Balance**

Assumes that, on average, the colors in a scene should balance out to gray.
The mean of each of the R, G, B channels is computed, and each channel is
scaled so that its average matches the overall average of all three
channels. Since the red channel is the most attenuated underwater, this step
boosts red relative to green/blue and removes most of the teal cast.

**2. CLAHE (Contrast Limited Adaptive Histogram Equalization)**

Applied to the L channel of the LAB color space after white balancing. This
improves local contrast (the image is fairly flat/hazy after correction)
without touching the color channels (`a`, `b`), so it sharpens detail
without reintroducing a color cast.

## Pipeline

```
Input (BGR) → Gray World White Balance → Convert to LAB
            → CLAHE on L channel → Convert back to BGR → Output
```

## Files

- `color_correction.py` — implementation
- `input_image.png` — original image
- `output_image.png` — color-corrected result
- `comparison.png` — side-by-side before/after

## Result

The teal cast is largely removed, the background grid and card turn closer
to their true gray/white tones, and the crabs/tick figures become more
visually distinguishable from the background.
