# 3. Rozmycie dwustronne w praktyce
# a. Załaduj zdjęcie zawierające zarówno szum, jak i ostre krawędzie.
# b. Zastosuj rozmycie dwustronne (cv2.bilateralFilter) z różnymi wartościami
# parametrów.
# c. Porównaj efekty z innymi metodami rozmycia.

import cv2
import numpy as np

image = cv2.imread("pies_w_deszczu.png")

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


cv2.destroyAllWindows()
cv2.imshow("Original", image)
params2 = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for (diameter, sigmaColor, sigmaSpace) in params2:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = "Blurred_2 d={}, sc={}, ss={}".format(
        diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)


# d. Odpowiedz na pytania (w formie komentarza w kodzie):
# i. Czy rozmycie dwustronne skutecznie redukuje szum? - raczej tak
# ii. Czy zachowuje lepiej krawędzie w porównaniu do innych metod? - prawie zawsze zachowuje lepiej
# iii. Jakie wartości parametrów dają najlepsze rezultaty?