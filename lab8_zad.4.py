# 4. Dynamiczny wybór ROI
# a. Napisz skrypt, który pozwala użytkownikowi podać wartości startX , endX ,
# startY , endY z klawiatury.
# b. Przytnij obraz zgodnie z wprowadzonymi wartościami i wyświetl wynik.

import cv2
import numpy as np

def zad4():
    image = cv2.imread("zdjecie_psa.png")


    height, width = image.shape[:2]
    print(f"Width = {width}px, height = {height}px")
    print("Insert coordinates to crop (ROI).")

    try:
        startX = int(input(f"startX (0 do {width-1}): "))
        endX = int(input(f"endX (startX do {width}): "))
        startY = int(input(f"startY (0 do {height-1}): "))
        endY = int(input(f"endY (startY do {height}): "))

        if not (0 <= startX < endX <= width and \
                0 <= startY < endY <= height):
            print("Wrong coordinates. Try again.")
            exit()

    except ValueError:
        print("Insert integer coordinates.")
        exit()

    roi = image[startY:endY, startX:endX]
    cv2.imshow("Original", image)
    cv2.imshow("Dynamiczne ROI", roi)

    cv2.waitKey(0)

zad4()
cv2.destroyAllWindows()