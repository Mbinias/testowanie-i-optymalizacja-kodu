# 8. Animacja przesuwającego się ROI
# a. Wczytaj obraz i dynamicznie przesuwaj ROI w poziomie (np. przesunięcie
# co 10 pikseli), aby stworzyć efekt „przesuwania kamery”.
# b. Wyświetlaj na ekranie kolejne wycinki ROI po kliknięciu w klawiature.

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original Image", image)
print("Press any key to pan the ROI. Press 'q' to quit.")

height, width = image.shape[:2]

roi_width = 200
roi_height = 400

if roi_width > width:
    roi_width = width
if roi_height > height:
    roi_height = height

current_startX = 0
current_startY = (height - roi_height) // 2

pan_step = 10

while True:
    current_endX = current_startX + roi_width
    current_endY = current_startY + roi_height

    if current_endX > width:
        current_startX = 0
        current_endX = roi_width

    roi = image[current_startY:current_endY, current_startX:current_endX]

    cv2.imshow("Panning ROI", roi)

    key = cv2.waitKey(0)

    if key == ord('q'):
        break
    else:
        current_startX += pan_step

cv2.destroyAllWindows()