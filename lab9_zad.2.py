# 2. Symulacja efektu "przepalenia" obrazu
# a. Dodaj do każdego piksela wartość 150, ale używając NumPy.
# b. Porównaj wynik z operacją cv2.add() .

import cv2
import numpy as np

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

M_np_burn = np.ones(image.shape, dtype="uint8") * 150
burned_np = image + M_np_burn
cv2.imshow("Przepalenie (NumPy)", burned_np)

M_cv2_add = np.ones(image.shape, dtype="uint8") * 150
added_cv2_compare = cv2.add(image, M_cv2_add)
cv2.imshow("Dodane (OpenCV, dla porownania)", added_cv2_compare)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Numpy powoduje dodawanie bardzo ciemnych kolorow, w miejscu, gdzie libczy przekroczyly 255
#Opencv powoduje, ze obraz jest bardzo jasny