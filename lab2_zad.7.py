import cv2

"""7. Wycięcie fragmentu obrazu
a. Podziel obraz na 9 równych części.
b. Pobierz fragment obrazu obejmujący środek.
c. Wyświetl wycięty fragment osobno."""

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]

(cX, cY) = (w // 3, h // 3)

tl = image[cY:2*cY, cX:2*cX]
cv2.imshow("middle", tl)

cv2.waitKey(0)