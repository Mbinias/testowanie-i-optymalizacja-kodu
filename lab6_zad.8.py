# 8. Efekty przy skalowaniu w górę
# a. Powiększ obraz 4× używając INTER_CUBIC i INTER_LANCZOS4 .
# b. Porównaj ostrość obrazu w obu przypadkach.

import cv2

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

new_width = int(image.shape[1] * 4)
new_height = int(image.shape[0] * 4)

dim = (new_width, new_height)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized", resized)

resized2 = cv2.resize(image, dim, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Resized2", resized2)

cv2.waitKey(0)