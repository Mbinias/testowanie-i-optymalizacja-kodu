# 1. Eksploracja różnych metod rozmycia
# a. Załaduj dowolny obraz i zastosuj do niego cztery różne metody rozmycia
# i. proste rozmycie cv2.blur
# ii. rozmycie Gaussa cv2.GaussianBlur
# iii. rozmycie medianowe cv2.medianBlur
# iv. rozmycie dwustronne cv2.bilateralFilter

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


# b. Dla każdej metody porównaj efekty wizualne przy różnych wartościach
# parametrów kernela. Odpowiedz na pytania (w formie komentarza w
# kodzie):
# i. Która metoda najlepiej usuwa szum? - zależy od rodzaju szumu
# ii. Która metoda zachowuje najwięcej szczegółów? - najwięcej szczegółów zachowuje metoda rozmycia dwustronnego
# iii. Jakie są zalety i wady każdej metody? -
# Proste rozmycie (cv2.blur): Szybkie, ale mocno rozmywa szczegóły i krawędzie.
# Rozmycie Gaussa (cv2.GaussianBlur): lepsze zachowanie szczegółów niż proste rozmycie, ale nadal rozmywa krawędzie.
# Rozmycie medianowe (cv2.medianBlur): dobrze zachowuje ostre krawędzie może tracić drobne detale.
# Rozmycie dwustronne (cv2.bilateralFilter): Najlepsze zachowanie szczegółów i krawędzi, skutecznie redukuje różne typy szumu,
# ale jest wolniejsze.