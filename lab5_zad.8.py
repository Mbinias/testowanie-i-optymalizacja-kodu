# 8. Obrót sekwencyjny
# a. Wykonaj trzy obroty po 30 stopni wokół środka obrazu i wyświetl wynik
# końcowy.
# b. Sprawdź, czy wynik różni się od pojedynczego obrotu o 90 stopni.

import numpy as np
import cv2
import argparse
import imutils

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotated = image
for i in range (3):
    rotated = imutils.rotate(rotated, 30)
    if i >= 2:
        cv2.imshow("Rotated by 90 Degrees1", rotated)

rotated2 = imutils.rotate(image, 90)
cv2.imshow("Rotated by 90 Degrees2", rotated2)

cv2.waitKey(0)
