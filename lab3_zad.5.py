# 5. Eksperymentowanie z pętlą
# a. Zmodyfikuj kod pętli rysującej okręgi, aby zamiast okręgów rysowała
# kwadraty. Każdy kolejny kwadrat powinien być większy o 20 pikseli od
# poprzedniego i mieć środek w tym samym miejscu.

import numpy as np
import cv2
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
white = (255, 255, 255)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

for r in range(0, 140, 20):
    cv2.rectangle(canvas, (centerX - r, centerY - r), (centerX + r, centerY + r), green)
    #cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)