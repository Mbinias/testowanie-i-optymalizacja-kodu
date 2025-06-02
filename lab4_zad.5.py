# 5. Dynamiczne przesunięcie na podstawie parametrów użytkownika
# a. Zmodyfikuj kod, aby użytkownik mógł podać wartości przesunięcia tx i ty
# poprzez wprowadzenie ich z klawiatury (np. przy użyciu input())
# b. Sprawdź, jak działa przesunięcie dla różnych wartości.

import numpy as np
import cv2
import imutils

image = cv2.imread('zdjecie_psa.png')


def przesuniecie():
    x = int(input("podaj wartosc x: "))
    y = int(input("podaj wartosc y: "))

    shifted_imutils = imutils.translate(image, x, y) # x_offset, y_offset

    cv2.imshow('image', image)
    cv2.imshow("Przesuniecie z imutils.translate", shifted_imutils)

przesuniecie()
cv2.waitKey(0)