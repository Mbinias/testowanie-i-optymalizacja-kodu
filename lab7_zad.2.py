# 2. Odbicie pionowe
# a. Wykonaj odbicie lustrzane w pionie.
# b. Porównaj wynik z obrazem oryginalnym.

import cv2
image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original", image)
print("[INFO] flipping image vertically")
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped vertically", flipped)

cv2.waitKey(0)