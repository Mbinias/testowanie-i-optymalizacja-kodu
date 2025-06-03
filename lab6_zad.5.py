# 5. Automatyczne skalowanie na podstawie szerokości
# a. Zmień szerokość obrazu na 500 pikseli, zachowując proporcje.
# b. Użyj imutils.resize() .

import cv2
import imutils

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

resized = imutils.resize(image, width=500)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)