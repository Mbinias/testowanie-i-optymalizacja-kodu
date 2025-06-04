# 2. Analiza wpływu rozmiaru kernela na efekt rozmycia
# a. Zastosuj każdą z metod rozmycia do obrazu, używając różnych wartości
# kernela: (3x3), (5x5), (9x9), (15x15).

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")

cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]
for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)

    cv2.waitKey(0)


cv2.destroyAllWindows()
cv2.imshow("Original", image)
for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)


cv2.destroyAllWindows()
cv2.imshow("Original", image)
for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurred)
    cv2.waitKey(0)


cv2.destroyAllWindows()
cv2.imshow("Original", image)
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = "Blurred d={}, sc={}, ss={}".format(
        diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)


# b. Porównaj wyniki i odpowiedz na pytania (w formie komentarza w kodzie):
# i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
# - im większy jest kernel, tym większe rozmycie i mniej widoczne szczegóły
# ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty
# istotnych detali? - mały (3x3) lub średni (5x5) w zależności od poziomu szumu