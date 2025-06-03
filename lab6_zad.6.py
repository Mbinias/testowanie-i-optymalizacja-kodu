# 6. Automatyczne skalowanie na podstawie wysokości
# a. Zmień wysokość obrazu na 400 pikseli, zachowując proporcje.
# b. Wyświetl wynik.

import cv2
import imutils

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

resized = imutils.resize(image, height=400)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)