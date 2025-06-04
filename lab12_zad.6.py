# 6. Eksperymentowanie z logiem OpenCV
# a. Pobierz logo OpenCV i rozdziel jego kanały.
# b. Spróbuj zamienić kolory tak, aby wyglądało inaczej, np. zamienić niebieski
# z czerwonym.
# c. Spróbuj usunąć jeden kanał całkowicie i sprawdź, jak wpłynie to na wygląd
# loga.

import cv2
import numpy as np

logo = cv2.imread("logo.png")
cv2.imshow("Original OpenCV Logo", logo)

(B, G, R) = cv2.split(logo)

cv2.imshow("Logo Blue Channel", B)
cv2.imshow("Logo Green Channel", G)
cv2.imshow("Logo Red Channel", R)

swapped_rb = cv2.merge([R, G, B])
cv2.imshow("Swapped Red and Blue", swapped_rb)

swapped_gb = cv2.merge([G, B, R])
cv2.imshow("Swapped Green and Blue", swapped_gb)

zeros = np.zeros(logo.shape[:2], dtype="uint8")

no_blue_logo = cv2.merge([zeros, G, R])
cv2.imshow("Logo without Blue", no_blue_logo)

no_red_logo = cv2.merge([B, G, zeros])
cv2.imshow("Logo without Red", no_red_logo)

cv2.waitKey(0)
cv2.destroyAllWindows()