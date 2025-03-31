# 4. Złożona figura
# a. Narysuj na obrazie figurę składającą się z kwadratu o wymiarach 100x100
# px, wewnątrz którego znajduje się mniejszy okrąg o promieniu 30 px.
# Wszystko powinno być wycentrowane na obrazie.

import numpy as np
import cv2
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
white = (255, 255, 255)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

cv2.rectangle(canvas, (centerX-50, centerY-50), (centerX+50, centerY+50), green)
r=30
cv2.circle(canvas, (centerX,centerY), r, red)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)