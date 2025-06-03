# 3. Odbicie względem obu osi
# a. Odbij obraz zarówno poziomo, jak i pionowo (czyli względem obu osi).

import cv2
image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original", image)
print("[INFO] flipping image ")
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped ", flipped)

cv2.waitKey(0)