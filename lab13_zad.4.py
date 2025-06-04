# 4. Łączenie przerw w obiektach za pomocą zamknięcia
# a. Pobierz obraz zawierający znaki lub litery z przerwami w konturach.
# b. Wykorzystaj zamknięcie do połączenia fragmentów znaków i poprawienia
# ich czytelności.
# c. Porównaj efekty różnych kształtów elementów strukturalnych (np.
# prostokątnego, eliptycznego).

import cv2

image = cv2.imread('czcionka.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]
# loop over the kernels sizes again
for kernelSize in kernelSizes:
    # construct a rectangular kernel form the current size, but this
    # time apply a "closing" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(
    kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)
cv2.destroyAllWindows()

# możliwe, że w danym przypadku przerwy są zbyt duże lub zbyt nieregularne,
# ale przy kolejnych iteracjach jedynie się powiększają