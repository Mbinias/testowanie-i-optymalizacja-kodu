# 6. Przygotowanie własnego przykładu zastosowania operacji morfologicznych
# a. Wybierz realny przypadek użycia (np. poprawa czytelności tablic
# rejestracyjnych, usuwanie szumu z dokumentów zeskanowanych, analiza
# obrazów medycznych).
# b. Zastosuj odpowiednie operacje morfologiczne i zaprezentuj ich wpływ na
# poprawę jakości analizy obrazu.

import cv2
import numpy as np

image_path = "pies_w_deszczu.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

cv2.imshow("Original Image", image)
cv2.waitKey(0)

kernel_opening = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel_opening)
cv2.imshow("After Opening (Noise Filter)", opened_image)
cv2.waitKey(0)

kernel_closing = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel_closing) # Możesz zastosować na original_image lub na opened_image
cv2.imshow("After Closing (Gap Filling)", closed_image)
cv2.waitKey(0)

cv2.destroyAllWindows()