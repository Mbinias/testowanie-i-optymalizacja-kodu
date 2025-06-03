# 1. Porównanie metod dodawania
# a. Wczytaj obraz i zwiększ jego jasność o 50 przy użyciu zarówno NumPy,
# jak i OpenCV.
# b. Sprawdź, jak różnią się wyniki.

import cv2
import numpy as np

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

M_cv2 = np.ones(image.shape, dtype="uint8") * 50
added_cv2 = cv2.add(image, M_cv2)
cv2.imshow("Jasniej (OpenCV)", added_cv2)

M_np = np.ones(image.shape, dtype="uint8") * 50
added_np = image + M_np
cv2.imshow("Jasniej (NumPy)", added_np)

cv2.waitKey(0)
cv2.destroyAllWindows()

# numpy przechodzi poza zakres i w niektórych miejscach zdjecia robi prawie negatyw,
# opencv pozostawia jasne obszary bez zawijania