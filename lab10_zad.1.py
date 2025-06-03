# 1. Kombinacja różnych kształtów i operacji bitowych
# a. Narysuj trójkąt i porównaj go z okręgiem, wykorzystując różne operacje
# bitowe ( AND , OR , XOR , NOT ).
# b. Sprawdź, jak zmieniają się wyniki w zależności od pozycji kształtów.

import numpy as np
import cv2

image_size = 300
triangle = np.zeros((image_size, image_size), dtype="uint8")
circle_img = np.zeros((image_size, image_size), dtype="uint8") # Zmieniono nazwę, aby nie kolidować z 'circle'

pts = np.array([[150, 50], [50, 250], [250, 250]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(triangle, [pts], 255)
cv2.imshow("Triangle", triangle)


cv2.circle(circle_img, (150, 150), 100, 255, -1)
cv2.imshow("Circle", circle_img)

bitwiseAnd_tc = cv2.bitwise_and(triangle, circle_img)
cv2.imshow("Triangle AND Circle", bitwiseAnd_tc)

bitwiseOr_tc = cv2.bitwise_or(triangle, circle_img)
cv2.imshow("Triangle OR Circle", bitwiseOr_tc)

bitwiseXor_tc = cv2.bitwise_xor(triangle, circle_img)
cv2.imshow("Triangle XOR Circle", bitwiseXor_tc)

bitwiseNot_t = cv2.bitwise_not(triangle)
cv2.imshow("NOT Triangle", bitwiseNot_t)

cv2.waitKey(0)

triangle_shifted = np.zeros((image_size, image_size), dtype="uint8")
circle_shifted = np.zeros((image_size, image_size), dtype="uint8")

pts_shifted = np.array([[200, 100], [100, 300], [300, 300]], np.int32)
pts_shifted = pts_shifted.reshape((-1, 1, 2))
cv2.fillPoly(triangle_shifted, [pts_shifted], 255)
cv2.imshow("Triangle Shifted", triangle_shifted)

cv2.circle(circle_shifted, (100, 100), 100, 255, -1)
cv2.imshow("Circle Shifted", circle_shifted)

bitwiseAnd_shifted = cv2.bitwise_and(triangle_shifted, circle_shifted)
cv2.imshow("Shifted Triangle AND Circle", bitwiseAnd_shifted)

bitwiseOr_shifted = cv2.bitwise_or(triangle_shifted, circle_shifted)
cv2.imshow("Shifted Triangle OR Circle", bitwiseOr_shifted)

bitwiseXor_shifted = cv2.bitwise_xor(triangle_shifted, circle_shifted)
cv2.imshow("Shifted Triangle XOR Circle", bitwiseXor_shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()