# 1. Wybór ROI na podstawie współrzędnych
# a. Zdefiniuj ROI, który obejmuje lewy górny róg obrazu o wymiarach 100x100
# pikseli.
# b. Wyświetl wynik.

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")

roi = image[0:100, 0:100]

cv2.imshow("ROI ", roi)

cv2.waitKey(0)