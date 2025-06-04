# 4. Analiza wpływu rozmycia na tekst na obrazie
# a. Znajdź lub przygotuj obraz zawierający tekst (np. logo, znak drogowy,
# nagłówek gazety).
# b. Zastosuj różne metody rozmycia (cv2.blur, cv2.GaussianBlur,
# cv2.medianBlur, cv2.bilateralFilter) z różnymi parametrami.
# c. Odpowiedz na pytania:
# i. Które metody najmocniej rozmywają tekst?
# ii. Które pozwalają zachować jego czytelność?

import cv2
import numpy as np

image_path = "czcionka.png"

image = cv2.imread(image_path)

cv2.imshow("Original Text Image", image)
cv2.waitKey(0)

kernel_sizes_small = [(3, 3), (5, 5), (7, 7)]
kernel_sizes_large = [(9, 9), (15, 15), (25, 25)]

for (kX, kY) in kernel_sizes_large:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow(f"Average Blur ({kX},{kY})", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()

for (kX, kY) in kernel_sizes_large:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow(f"Gaussian Blur ({kX},{kY})", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()

for k in [3, 5, 7, 15]:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Median Blur ({k})", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()

bilateral_params = [(11, 21, 7), (21, 41, 21), (31, 61, 39)]

for (diameter, sigmaColor, sigmaSpace) in bilateral_params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    cv2.imshow(f"Bilateral d={diameter}, sc={sigmaColor}, ss={sigmaSpace}", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()

#Najmocniej rozmywają tekst: cv2.blur i cv2.GaussianBlur
#Zachowują czytelność tekstu: cv2.medianBlur i cv2.bilateralFilter- najlepiej