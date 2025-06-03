# 7. Efekty przy skalowaniu w dół
# a. Zmniejsz obraz 5× przy użyciu INTER_AREA .
# b. Sprawdź, jak zmienia się jakość w porównaniu do innych metod.

import cv2

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

new_width = int(image.shape[1] * 0.2)
new_height = int(image.shape[0] * 0.2)

dim = (new_width, new_height)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)

resized2 = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized2", resized2)

cv2.waitKey(0)

# Inter area zachowuje znacznie lepsza jakosc