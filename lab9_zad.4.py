# 4. Tworzenie własnego "filtra Instagram":
# a. Dodaj do kanału czerwonego +30, do zielonego -20, a do niebieskiego
# +10.
# b. Sprawdź, jak zmienia się obraz.

import cv2
import numpy as np

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

b, g, r = cv2.split(image)

r_filtered = cv2.add(r, np.uint8([30]))

g_filtered = cv2.subtract(g, np.uint8([20]))

b_filtered = cv2.add(b, np.uint8([10]))

filtered_image = cv2.merge([b_filtered, g_filtered, r_filtered])
cv2.imshow("Instagram Filter", filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#obraz wydaje sie bardziej rozowy