# 5. Zastosowanie maski do selektywnej modyfikacji kanałów
# a. czytaj obraz i stwórz maskę obejmującą tylko wybrany obiekt (np.
# czerwony samochód).
# b. Wykorzystując maskę, zwiększ nasycenie koloru czerwonego tylko w tej
# części obrazu.

import cv2
import numpy as np

image = cv2.imread("logo.png")
cv2.imshow("Original Image", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask_red_object = cv2.bitwise_or(mask1, mask2)
cv2.imshow("Red Object Mask", mask_red_object)

(B, G, R) = cv2.split(image)

R_modified = R.copy()

R_modified = cv2.add(R_modified, 70, mask=mask_red_object)

result_image = cv2.merge([B, G, R_modified])
cv2.imshow("Red Boosted in Masked Area", result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()