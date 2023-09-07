# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:19:08 2023

@author: HP
"""

import cv2
import os

input_directory = 'Datasets\DB1_B'
output_directory = 'newDatasets'



for filename in os.listdir(input_directory):
        print(filename)
        path=os.path.join(input_directory, filename)
        print(path)
        image = cv2.imread(path)

        height, width = image.shape[:2]

        resized_image = cv2.resize(image, (width // 2, height // 2))

        cv2.imwrite(os.path.join(output_directory, filename), resized_image)
        
        print(f'Resized {filename}')

print('Done resizing images.')
