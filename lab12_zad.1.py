# 1. Wyświetlenie pojedynczych kanałów na obrazie
# a. Wczytaj dowolny obraz.
# b. Rozdziel kanały B, G, R i wyświetl je osobno.
# c. Zapisz te kanały jako osobne obrazy.

import cv2
import numpy as np

image = cv2.imread("logo.png")
(B, G, R) = cv2.split(image)

cv2.imshow("Blue Channel", B)
cv2.imshow("Green Channel", G)
cv2.imshow("Red Channel", R)

cv2.imwrite("blue_channel.jpg", B)
cv2.imwrite("green_channel.jpg", G)
cv2.imwrite("red_channel.jpg", R)
print("Channels saved as 'blue_channel.jpg', 'green_channel.jpg', 'red_channel.jpg'")

cv2.waitKey(0)
cv2.destroyAllWindows()