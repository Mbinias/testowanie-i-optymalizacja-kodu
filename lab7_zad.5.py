# 5. Zastosowanie odbicia na wybranym obszarze
# a. Wczytaj obraz i wytnij z niego fragment (np. środek obrazu lub prawą
# połowę).
# b. Odbij tylko wycięty fragment i wklej go z powrotem do obrazu.

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")
(h, w) = image.shape[:2]

x_start, y_start = w // 4, h // 4
x_end, y_end = 3 * w // 4, 3 * h // 4

region = image[y_start:y_end, x_start:x_end]

flipped_region = cv2.flip(region, 1)

image[y_start:y_end, x_start:x_end] = flipped_region

cv2.imshow("Region", image)
cv2.waitKey(0)