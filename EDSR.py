# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:43:24 2023

@author: HP
"""

import cv2
from cv2 import dnn_superres

#intialize superresolution object
sr=dnn_superres.DnnSuperResImpl_create()

#read the model
path='EDSR_x2.pb'
sr.readModel(path)

#set the model and scale
sr.setModel('edsr',2)
