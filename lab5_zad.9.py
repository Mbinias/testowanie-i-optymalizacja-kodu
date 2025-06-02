# 9. Obrót i zapis obrazu
# a. Obróć obraz o 75 stopni i zapisz wynik do pliku rotated_output.jpg .

import numpy as np
import cv2
import argparse
import imutils

image = cv2.imread('zdjecie_psa.png')

rotated = imutils.rotate(image, 75)

cv2.imwrite('rotated_output.jpg', rotated)

cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)