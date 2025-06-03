# 1. Zmniejszenie obrazu o połowę
# a. Wczytaj obraz i zmniejsz jego szerokość oraz wysokość o 50%.
# b. Wyświetl wynik.

import cv2

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

new_width = int(image.shape[1] * 0.5)
new_height = int(image.shape[0] * 0.5)

dim = (new_width, new_height)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
