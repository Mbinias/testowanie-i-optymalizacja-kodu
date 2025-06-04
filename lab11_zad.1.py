# 1. Maskowanie obszaru twarzy
# a. Wczytaj zdjęcie osoby.
# b. Stwórz maskę pozostawiającą twarz osoby (np. prostokąt lub elipsa).
# c. Zastosuj maskę na obrazie i wyświetl wynik.

import cv2
import numpy as np

image = cv2.imread("Gandalf.jpg")
cv2.imshow("Original Image", image)

(h, w) = image.shape[:2]
face_center_x = w // 2
face_center_y = h // 2
face_width = 150
face_height = 200

mask = np.zeros(image.shape[:2], dtype="uint8")

cv2.ellipse(mask, (face_center_x, face_center_y - 30), (face_width // 2, face_height // 2), 0, 0, 360, 255, -1)

cv2.imshow("Face Mask", mask)

masked_face = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Face", masked_face)

cv2.waitKey(0)
cv2.destroyAllWindows()