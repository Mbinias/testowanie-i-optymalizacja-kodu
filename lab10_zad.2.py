# 2. Zastosowanie operacji XOR do wykrywania różnic między obrazami
# a. Wczytaj dwa podobne obrazy z drobnymi różnicami.
# b. Użyj cv2.bitwise_xor , aby uwidocznić różnice między nimi.

import cv2
import numpy as np

image1 = cv2.imread('zdjecie_psa.png')

M = np.float32([[1, 0, 5], [0, 1, 5]])
image2 = cv2.warpAffine(image1, M, (image1.shape[1], image1.shape[0]))

cv2.imshow("Image 1 (Original)", image1)
cv2.imshow("Image 2 (Modified)", image2)

difference_xor = cv2.bitwise_xor(image1, image2)
cv2.imshow("Differences (XOR)", difference_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()