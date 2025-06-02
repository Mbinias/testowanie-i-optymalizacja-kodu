# 7. Porównanie warpAffine i imutils.rotate
# a. Wykonaj obrót o 60 stopni dwoma sposobami: za pomocą cv2.warpAffine i
# imutils.rotate .
# b. Porównaj wyniki i zwróć uwagę na różnice.

import numpy as np
import cv2
import argparse
import imutils

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# cv2.imshow("Original", image)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

rotated2 = imutils.rotate(image, 60)
cv2.imshow("Rotated by 180 Degrees", rotated2)

cv2.waitKey(0)