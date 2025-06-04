# 2. Analiza cech uwidaczniających się w poszczególnych kanałach
# a. Wybierz obraz, na którym znajdują się obiekty o różnych kolorach.
# b. Porównaj, jak różne elementy obrazu są widoczne w poszczególnych
# kanałach B, G, R.
# c. Spróbuj znaleźć taki obiekt, który jest wyraźnie widoczny tylko na jednym
# z kanałów.

import cv2

image = cv2.imread("logo.png")
cv2.imshow("Original Color Image", image)

(B, G, R) = cv2.split(image)

cv2.imshow("Blue Channel (Analysis)", B)
cv2.imshow("Green Channel (Analysis)", G)
cv2.imshow("Red Channel (Analysis)", R)

cv2.waitKey(0)
cv2.destroyAllWindows()