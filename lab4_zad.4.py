# 4. Wykorzystanie funkcji imutils.translate
# a. Przesuń obraz o 50 pikseli w dół i 100 pikseli w prawo za pomocą
# imutils.translate .
# b. Porównaj wynik z przesunięciem wykonanym wcześniej przez cv2.warpAffine .
# Czy zauważyłeś różnice?

import numpy as np
import cv2
import imutils

image = cv2.imread('zdjecie_psa.png')
cv2.imshow('image', image)

shifted_imutils = imutils.translate(image, 100, 50) # x_offset, y_offset
cv2.imshow("Przesuniecie z imutils.translate", shifted_imutils)

cv2.waitKey(0)

#nie zauwazylem roznicy, ale ten sposob jest w tym przypadku szybszy