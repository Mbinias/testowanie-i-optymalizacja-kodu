# 2. Ukrywanie określonego obszaru twarzy
# a. Wczytaj zdjęcie osoby.
# b. Stwórz maskę zasłaniającą oczy (np. prostokąt lub elipsa).
# c. Zastosuj maskę na obrazie i wyświetl wynik.

import cv2
import numpy as np

# a. Wczytaj zdjęcie osoby.
image = cv2.imread("Gandalf.jpg") # Użyj tego samego zdjęcia osoby
if image is None:
    print("Error: Could not load image. Make sure 'Gandalf.jpg' is in the same directory.")
    exit()

cv2.imshow("Original Image", image)

mask_hide = np.ones(image.shape[:2], dtype="uint8") * 255

left_eye_x = 95
left_eye_y = 59
eye_width = 25
eye_height = 13

right_eye_x = 150
right_eye_y = 59

cv2.rectangle(mask_hide, (left_eye_x, left_eye_y),
              (left_eye_x + eye_width, left_eye_y + eye_height), 0, -1)
cv2.rectangle(mask_hide, (right_eye_x, right_eye_y),
              (right_eye_x + eye_width, right_eye_y + eye_height), 0, -1)

cv2.imshow("Mask to Hide Eyes", mask_hide)

hidden_eyes_image = cv2.bitwise_and(image, image, mask=mask_hide)
cv2.imshow("Hidden Eyes", hidden_eyes_image)

cv2.waitKey(0)
cv2.destroyAllWindows()