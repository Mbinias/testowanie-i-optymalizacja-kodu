import cv2

"""3. Znajdowanie środka obrazu
a. Wczytaj obraz i oblicz współrzędne jego środka.
b. Pobierz wartość koloru piksela w tym miejscu i wyświetl ją w konsoli."""

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]

#cv2.imshow("Original", image)
#cv2.waitKey(0)
cv2.destroyAllWindows()
(cX, cY) = (w // 2, h // 2)
print (f"cX:{cX}, cY:{cY}")
(b, g, r) = image[cX, cY]
print("Pixel at the middle - Red: {}, Green: {}, Blue: {}".format(r, g, b))