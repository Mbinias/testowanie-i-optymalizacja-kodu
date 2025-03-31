import cv2

"""2. Modyfikacja pojedynczego piksela
a. Zmień kolor piksela w prawym dolnym rogu obrazu na czerwony (0, 0, 255) .
b. Wyświetl obraz przed i po zmianie."""

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image[h-1, w-1] = (0, 0, 255)
(b, g, r) = image[h-1, w-1]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

