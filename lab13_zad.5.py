# 5. Eksperymentowanie z różnymi elementami strukturalnymi
# a. Wybierz jeden obraz testowy i wykonaj na nim wszystkie podstawowe
# operacje morfologiczne (erozja, dylatacja, otwarcie, zamknięcie, gradient).
# b. Powtórz eksperyment, zmieniając kształt elementu strukturalnego (np.
# kwadrat, krzyż, elipsa).
# c. Porównaj wyniki i opisz, jakie różnice zauważasz w przetworzonych
# obrazach.

import cv2

image = cv2.imread('figury_2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

#erozja
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    cv2.waitKey(0)

# dylatacja
cv2.destroyAllWindows()
cv2.imshow("Original", image)
# apply a series of dilations
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    cv2.waitKey(0)

#otwarcie
cv2.destroyAllWindows()
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]

for kernelSize in kernelSizes:

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(
    kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)

#zamknięcie
cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernelSizes:

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(
    kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

#gradient morfologiczny
cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernelSizes:

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(
    kernelSize[0], kernelSize[1]), gradient)
    cv2.waitKey(0)

#erozja zmniejsza elementy na obrazie, a dylatacja je zwiększa, otwarcie w tym przypadku nie daje
# konkretnych efektów, natomiast zamknięcie zwiększa bardzo dobrze wyrazistość poszczególnych elementów
# gradient zwiększa wyrazistość i różnicę między elementami i tłem