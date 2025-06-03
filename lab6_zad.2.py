# 2. Powiększenie obrazu dwukrotnie
# a. Powiększ obraz 2× zarówno w pionie, jak i w poziomie.
# b. Użyj metody cv2.INTER_LINEAR .

import cv2

image = cv2.imread('zdjecie_psa.png')
cv2.imshow("Original", image)

new_width = int(image.shape[1] * 2)
new_height = int(image.shape[0] * 2)

dim = (new_width, new_height)
# perform the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
