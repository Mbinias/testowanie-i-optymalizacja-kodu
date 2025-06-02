# 4. Obrót o dowolny kąt
# a. Pobierz od użytkownika kąt obrotu i wykonaj rotację wokół środka obrazu.
# b. Wyświetl wynik.

import numpy as np
import cv2
import argparse
import imutils

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# cv2.imshow("Original", image)

degree = int (input("podaj kat obrotu"))

M = cv2.getRotationMatrix2D((cX, cY), degree, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by given degrees", rotated)

cv2.waitKey(0)