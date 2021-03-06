# -*- coding: utf-8 -*-
"""1603045_lab_assignment_on_smoothing_sharpening_in_spatial_and_frequency_domain.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z4ANLdisJZJQHjH00ariv0396enymxHb
"""

import numpy as np
from scipy import ndimage
import cv2


image = cv2.imread('/content/drive/MyDrive/Colab Notebooks/lowcontrastfeattt-800x420.jpg', 0)

from google.colab.patches import cv2_imshow
cv2.imshow(image)
print(image.shape)

average_filter = 0.25 * np.array([[1, 1], [1,1]])
average_filter_output_image = ndimage.convolve(image, average_filter)
cv2.imshow(average_filter_output_image)
print(average_filter_output_image.shape)

laplacian_filter = np.array([[-1, -1, -1], \
                             [-1, 8, -1], \
                             [-1, -1, -1] ])

laplacian_filter_output_image = ndimage.convolve(image, laplacian_filter)
cv2.imshow(laplacian_filter_output_image)

low_pass_filter = np.array([[0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0], \
                            [0, 0, 1, 0, 0], \
                            [0, 0, 0, 0, 0], \
                            [0, 0, 0, 0, 0] ])
lowpass_output_image = ndimage.convolve(image, low_pass_filter)
cv2.imshow(lowpass_output_image)

high_pass_filter = np.array([[1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1], \
                            [1, 1, 0, 1, 1], \
                            [1, 1, 1, 1, 1], \
                            [1, 1, 1, 1, 1] ])

highpass_output_image = ndimage.convolve(image, high_pass_filter)
cv2.imshow(highpass)
print(highpass.shape)

