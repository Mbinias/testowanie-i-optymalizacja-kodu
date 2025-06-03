# 5. Zastosowanie arytmetyki do detekcji zmian w obrazach
# a. Wczytaj dwa obrazy tej samej sceny, ale z niewielkimi różnicami (np.
# obiekt przesunięty).
# b. Oblicz ich różnicę ( cv2.absdiff(image1, image2) ).
# c. Zinterpretuj wynik – jakie zmiany są widoczne?

import cv2
import numpy as np

image1 = cv2.imread('zdjecie_psa.png')

M = np.float32([[1, 0, 50], [0, 1, 0]])
image2 = cv2.warpAffine(image1, M, (image1.shape[1], image1.shape[0]))

cv2.imshow("Obraz 1 (oryginalny)", image1)
cv2.imshow("Obraz 2 (przesuniety w prawo)", image2)

difference = cv2.absdiff(image1, image2)
cv2.imshow("Obraz roznicowy", difference)

cv2.waitKey(0)
cv2.destroyAllWindows()