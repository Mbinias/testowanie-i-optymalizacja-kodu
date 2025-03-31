import cv2

"""5. Kolorowanie fragmentu obrazu
a. Podziel obraz na 4 równe części (ćwiartki).
b. Wypełnij lewą górną ćwiartkę kolorem niebieskim (255, 0, 0) .
c. Wyświetl obraz po zmianach."""

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
# set the top-left corner of the original image to be green
image[0:cY, 0:cX] = (255, 0, 0)
# Show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)