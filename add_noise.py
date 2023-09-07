# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:19:22 2023

@author: HP
"""

import numpy as np
import cv2

# Load an image
image = cv2.imread('porsche.jfif', cv2.IMREAD_COLOR)

# Add Gaussian noise to the image
mean = 0
stddev = 25
noisy_image = image + np.random.normal(mean, stddev, image.shape)

# Clip values to ensure they remain within the valid range
noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

# Save the noisy image
cv2.imwrite('noisy_image.jpg', noisy_image)