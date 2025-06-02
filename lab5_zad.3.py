# 3. Obrót wokół narożnika
# a. Obróć obraz o 30 stopni względem lewego górnego narożnika (0,0).
# b. Wyświetl wynik.

import numpy as np
import cv2
import argparse
import imutils

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# cv2.imshow("Original", image)

M = cv2.getRotationMatrix2D((0, 0), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Arbitrary Point", rotated)

cv2.waitKey(0)