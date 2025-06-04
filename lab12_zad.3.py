# 3. Rekonstrukcja obrazu po manipulacji kanałami
# a. Zamień wartości kanałów miejscami, np. wyświetl obraz w kolejności R, B,
# G.
# b. Ustaw wartość jednego z kanałów na zero i zobacz, jak zmienia się wygląd
# obrazu.

import cv2
import numpy as np

image = cv2.imread("logo.png") # Użyj dowolnego obrazu
cv2.imshow("Original Image", image)

(B, G, R) = cv2.split(image)

merged_rbg = cv2.merge([R, B, G])
cv2.imshow("Merged (R, B, G)", merged_rbg)

zeros = np.zeros(image.shape[:2], dtype="uint8")
merged_no_red = cv2.merge([B, G, zeros])
cv2.imshow("No Red Channel", merged_no_red)

merged_no_blue = cv2.merge([zeros, G, R])
cv2.imshow("No Blue Channel", merged_no_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()