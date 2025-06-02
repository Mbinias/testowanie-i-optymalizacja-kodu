# 6. Obrót bez przycinania ( rotate_bound )
# a. Wykorzystaj imutils.rotate_bound , aby obrócić obraz o -33 stopnie i uniknąć
# przycięcia.
# b. Wyświetl wynik.

import numpy as np
import cv2
import argparse
import imutils

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotated = imutils.rotate_bound(image, -33)

cv2.imshow("Rotated bound by -33", rotated)

cv2.waitKey(0)