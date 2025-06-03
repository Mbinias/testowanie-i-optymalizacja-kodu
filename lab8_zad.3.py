# 3. Przycięcie prawej połowy obrazu
# a. Przycięcie prawej połowy obrazu
# b. Wyświetl tylko prawą połowę.

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original", image)

height, width = image.shape[:2]
mid_width = width // 2

left_half = image[0:height, 0:mid_width]
right_half = image[0:height, mid_width:width]

cv2.imshow("right half", right_half)

cv2.waitKey(0)
cv2.destroyAllWindows()