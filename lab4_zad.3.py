# 3. Eksperymentowanie z dużymi wartościami przesunięcia
# a. Przesuń obraz o więcej niż połowę jego szerokości i wysokości.
# b. Sprawdź, co dzieje się z pikselami, które wychodzą poza zakres
# oryginalnego obrazu.

import numpy as np
import cv2

image = cv2.imread('zdjecie_psa.png')
cv2.imshow('image', image)

M = np.float32([
[1, 0, 250],
[0, 1, -350]
])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

cv2.waitKey(0)

#piksele, które wychodzą poza zakres oryginalnego obrazu nie są wyświetlane