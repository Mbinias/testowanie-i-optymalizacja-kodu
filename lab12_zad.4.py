# 4. Wzmocnienie jednego z kanałów
# a. Zwiększ intensywność jednego z kanałów (np. kanału czerwonego) i
# zaobserwuj, jak wpływa to na końcowy wygląd obrazu.
# b. Możesz to zrobić poprzez dodanie stałej wartości do danego kanału, np. R
# = cv2.add(R, 50) .

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original Image", image)

(B, G, R) = cv2.split(image)

R_boosted = cv2.add(R, 50)

merged_boosted_red = cv2.merge([B, G, R_boosted])
cv2.imshow("Boosted Red Channel", merged_boosted_red)

G_boosted = cv2.add(G, 50)
merged_boosted_green = cv2.merge([B, G_boosted, R])
cv2.imshow("Boosted Green Channel", merged_boosted_green)

cv2.waitKey(0)
cv2.destroyAllWindows()