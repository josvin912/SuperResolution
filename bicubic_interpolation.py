# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 19:41:41 2023

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# Load a small grayscale image (replace 'small_image.jpg' with your image)
small_image = plt.imread('fingerprint.jfif')

# Define the scaling factor for enlargement (e.g., 2 means doubling the size)
scaling_factor = 2


# Perform bicubic interpolation using scipy's zoom function
enlarged_image = ndimage.zoom(small_image, (scaling_factor, scaling_factor,1), order=3)
#order = 3 is to indicate this have to be done by using bicubic interpolation and 1 to indicate this is a color image RGB

output_file = 'enlarged_fingerprint_image.jpg'
plt.imsave(output_file, enlarged_image)

# Plot the original and enlarged images
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(small_image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(enlarged_image)
plt.title('Enlarged Image (Bicubic)')
plt.axis('off')

plt.tight_layout()
plt.show()

print(f'Enlarged image saved as {output_file}')

small_image.shape
enlarged_image.shape


