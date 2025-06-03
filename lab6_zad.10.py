# 10. Zmiana rozmiaru i zapis pliku
# a. Powiększ obraz do szerokości 800 pikseli i zapisz wynik do pliku
# resized_output.jpg .

import cv2
import imutils

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

resized = imutils.resize(image, width=800)
cv2.imshow("Resized via imutils", resized)
cv2.imwrite("resized_output.jpg", resized)
cv2.waitKey(0)