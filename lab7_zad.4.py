# 4. Porównanie efektów
# a. Wyświetl cztery wersje obrazu:
# i. Oryginał
# ii. Odbicie poziome
# iii. Odbicie pionowe
# iv. Odbicie względem obu osi

import cv2
image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped ", flipped)

flipped2 = cv2.flip(image, 0)
cv2.imshow("Flipped 2", flipped2)

flipped3 = cv2.flip(image, -1)
cv2.imshow("Flipped 3", flipped3)

cv2.waitKey(0)