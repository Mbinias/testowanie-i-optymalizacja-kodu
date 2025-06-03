# 9. Dynamiczna zmiana rozmiaru w pętli
# a. Stopniowo zwiększaj rozmiar obrazu od 100% do 300% w krokach co
# 20%.
# b. Wyświetl każdą wersję na ekranie z krótkim opóźnieniem ( cv2.waitKey(500) ).

import cv2
import numpy as np

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

scales = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0]

for scale in scales:
    new_width = int(image.shape[1] * scale)
    new_height = int(image.shape[0] * scale)
    dim = (new_width, new_height)

    resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(f"Skalowanie: {int(scale * 100)}%", resized)

    cv2.waitKey(500)
cv2.waitKey(0)
cv2.destroyAllWindows()