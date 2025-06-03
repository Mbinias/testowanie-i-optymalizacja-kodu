# 3. Zmiana rozmiaru na konkretną wartość
# a. Zmień rozmiar obrazu na dokładnie 200×300 pikseli.
# b. Użyj cv2.resize().

import cv2

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

target_width = 200
target_height = 300
dim_target = (target_width, target_height)

resized = cv2.resize(image, dim_target, interpolation=cv2.INTER_AREA)

cv2.imshow("Resized", resized)
cv2.waitKey(0)