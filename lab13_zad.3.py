# 3. Usuwanie szumu za pomocą otwarcia
# a. Wczytaj obraz z szumem (np. solnym i pieprzowym) i/lub obrazy typu
# Google Captcha.
# b. Zastosuj operację otwarcia z różnymi rozmiarami elementu strukturalnego.
# c. Porównaj wyniki przed i po operacji, oceniając skuteczność usuwania
# szumu.

import cv2

image = cv2.imread('Noise_salt_and_pepper.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]
# loop over the kernels sizes
for kernelSize in kernelSizes:
    # construct a rectangular kernel from the current size and then
    # apply an "opening" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(
    kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)
cv2.destroyAllWindows()

#Prawdopodobnie przez mały rozmiar zdjęcia tylko pierwsza operacja otwarcia poprawia jakość obrazu.
#Każda kolejna ma zbyt duży wpływ na całość i psuje jakość