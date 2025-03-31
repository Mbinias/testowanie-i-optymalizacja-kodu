import cv2

"""8. Modyfikacja całego wiersza pikseli
Pobieranie i ustawianie wartości pikseli 10
a. Wczytaj obraz i zmień kolor wszystkich pikseli w 100. wierszu na zielony
(0, 255, 0) .
b. Wyświetl obraz przed i po zmianie."""

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]

cv2.imshow("Original", image)

image[99, :] = [0, 255, 0]

cv2.imshow("Updated", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
