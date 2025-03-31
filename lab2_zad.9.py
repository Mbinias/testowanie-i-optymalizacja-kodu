import cv2

"""9. Zmiana wartości pikseli w określonym zakresie
a. Wypełnij obszar od (50,50) do (100,100) kolorem białym (255, 255, 255) .
b. Wyświetl obraz przed i po zmianie."""

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]

cv2.imshow("Original", image)

image[50:101, 50:101] = [255, 255, 255]

cv2.imshow("Updated", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
