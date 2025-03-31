import cv2

"""6. Wypełnienie konkretnego obszaru obrazu jednolitym kolorem
Pobierz współrzędne środka obrazu.
Wypełnij kwadrat o wymiarach 100x100 px, którego środek pokrywa się ze
środkiem obrazu, kolorem czerwonym (0, 0, 255) .
Wyświetl obraz po zmianach."""

image = cv2.imread('zdjecie_psa.png')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

image[cY-50:cY+50, cX-50:cX+50] = (0, 0, 255)

cv2.imshow("Updated", image)
cv2.waitKey(0)