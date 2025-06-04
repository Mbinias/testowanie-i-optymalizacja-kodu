# 3. Wykorzystanie maski do ekstrakcji koloru
# a. Wczytaj kolorowy obraz (np. kwiaty, samochód).
# b. Stwórz maskę w taki sposób, aby pozostawić tylko jeden wybrany kolor, a
# resztę obrazu zaciemnić.
# c. Wskazówka: użyj konwersji obrazu do przestrzeni barw HSV i maskowania
# na podstawie zakresu kolorów.

import cv2
import numpy as np

image = cv2.imread("kwiaty.png")
cv2.imshow("Original Color Image", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

cv2.imshow("Color Mask", mask)

color_extracted_image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Color Extracted Image", color_extracted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()