# 3. Przyciemnianie obrazu
# a. Zmniejsz jasność obrazu o 80 jednostek.
# b. Porównaj, jak NumPy i OpenCV traktują wartości poniżej 0.

import cv2
import numpy as np

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

M_cv2_sub = np.ones(image.shape, dtype="uint8") * 80
darker_cv2 = cv2.subtract(image, M_cv2_sub)
cv2.imshow("Ciemniej (OpenCV)", darker_cv2)

M_np_sub = np.ones(image.shape, dtype="uint8") * 80
darker_np = image - M_np_sub
cv2.imshow("Ciemniej (NumPy)", darker_np)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Numpy powoduje powstawanie przeciwnych, bardzo jasnych kolorow, Opencv rownomiernie przyciemnia obraz