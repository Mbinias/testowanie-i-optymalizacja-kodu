# 2. Przycięcie dolnej połowy obrazu
# a. Podziel obraz na dwie równe części (górną i dolną).
# b. Wyświetl tylko dolną połowę.

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original", image)

height, width = image.shape[:2]
mid_height = height // 2

top_half = image[0:mid_height, 0:width]
bottom_half = image[mid_height:height, 0:width]

cv2.imshow("bottom half", bottom_half)

cv2.waitKey(0)
cv2.destroyAllWindows()