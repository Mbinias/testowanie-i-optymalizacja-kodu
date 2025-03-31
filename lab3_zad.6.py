# 6. Zamazywanie szczegółów na zdjęciu
# a. Znajdź w Internecie profilowe zdjęcie osoby.
# b. Czerwonymi kołami “zasłoń” osobie na zdjęciu oczy.
# c. Zielonym prostokątem “zasłoń” osobie na zdjęciu usta.
# d. Niebieskim okręgiem obejmij dookoła twarz osoby.

import cv2
import numpy as np
image = cv2.imread('Gandalf.jpg')
(h, w) = image.shape[:2]
(centerX, centerY) = (w // 2, h // 2)

blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
white = (255, 255, 255)

r=15
# cv2.circle(, (40,40), r, blue)
#image[50:101, 50:101] = [255, 255, 255]

cv2.circle(image, (int(w/2)+30, int(h/2)-30), r, red, -1)
cv2.circle(image, (int(w/2)-20, int(h/2)-30), r, red, -1)
cv2.rectangle(image, (centerX-20, centerY+20), (centerX+35, centerY+50), green, -1)
r2 = 80
cv2.circle(image, (int(w/2)+5, int(h/2)-10), r2, blue)


cv2.imshow("Original", image)
cv2.waitKey(0)