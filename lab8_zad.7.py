# 7. Podział obrazu na siatkę
# a. Podziel obraz na 9 równych części (3x3).
# b. Wyświetl wszystkie części osobno.

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original Image", image)

height, width = image.shape[:2]

cell_width = width // 3
cell_height = height // 3

for row in range(3):
    for col in range(3):
        start_y = row * cell_height
        end_y = (row + 1) * cell_height
        start_x = col * cell_width
        end_x = (col + 1) * cell_width

        cell_roi = image[start_y:end_y, start_x:end_x]

        cv2.imshow(f"Grid Part ({row+1},{col+1})", cell_roi)

cv2.waitKey(0)
cv2.destroyAllWindows()