# 3. Rysowanie okręgów, utwórz czarny obraz o wymiarach 300x300 pikseli i
# narysuj na nim:
# a. Niebieski okrąg o promieniu 40 px w lewym górnym rogu.
# b. Czerwony okrąg o promieniu 60 px w środku obrazu.

import numpy as np
import cv2
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
white = (255, 255, 255)


canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

r=40
cv2.circle(canvas, (40,40), r, blue)
r2=60
cv2.circle(canvas, (centerX,centerY), r, red)




cv2.imshow("Canvas", canvas)
cv2.waitKey(0)