# 2. Eksperymentowanie z dylatacją
# a. Pobierz obraz zawierający cienkie linie lub przerwy między obiektami.
# b. Zastosuj dylatację z różnymi rozmiarami elementów strukturalnych.
# c. Przedstaw wykres lub tabelę pokazującą, jak zmienia się grubość
# obiektów w zależności od liczby iteracji dylatacji.

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('figury_2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
iterations = []
white_pixel_counts = []


cv2.imshow("Original", image)

for i in range(0, 6):
    dilated = cv2.dilate(binary.copy(), None, iterations=i + 1)
    white_pixels = cv2.countNonZero(dilated)
    iterations.append(i)
    white_pixel_counts.append(white_pixels)


    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    cv2.waitKey(0)
cv2.destroyAllWindows()

plt.plot(iterations, white_pixel_counts, marker='o')
plt.title("Zależność grubości obiektów od liczby iteracji dylatacji")
plt.xlabel("Liczba iteracji")
plt.ylabel("Liczba białych pikseli (grubość)")
plt.grid(True)
plt.show()