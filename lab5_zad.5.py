# 5. Obrót o 180 stopni za pomocą imutils.rotate
# a. Skorzystaj z imutils.rotate , aby obrócić obraz o 180 stopni.
# b. Wyświetl wynik.

import numpy as np
import cv2
import argparse
import imutils

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)

cv2.waitKey(0)