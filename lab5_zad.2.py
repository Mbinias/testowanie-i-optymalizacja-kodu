# 2. Obrót o -90 stopni
# a. Wczytaj obraz i obróć go o -90 stopni wokół środka.
# b. Wyświetl wynik.

import numpy as np
import cv2
import argparse
import imutils

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# cv2.imshow("Original", image)

M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

cv2.waitKey(0)