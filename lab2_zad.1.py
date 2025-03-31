import cv2

"""1. Odczyt wartości piksela
a. Wczytaj obraz i pobierz wartość piksela znajdującego się w lewym górnym
rogu (współrzędne 0,0 ).
b. Wyświetl wartości składowych koloru (R, G, B)."""

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()