import cv2

"""4. Zamiana wartości piksela na czarny
a. Pobierz od użytkownika współrzędne (x, y) .
b. Stwórz walidację, która zweryfikuje czy podane współrzędne nie
wychodzą poza wymiar zdjęcia.
c. Ustaw piksel w tym miejscu na czarny (0, 0, 0) ."""

def zmiana_na_czarny():
    x = int(input("Podaj x : "))
    y = int(input("Podaj y : "))
    image = cv2.imread('zdjecie_psa.png')
    (h, w) = image.shape[:2]
    if x < 0 or y < 0 or x > w - 1 or y > h - 1:
        print("niewlasciwe wspolrzedne")
        zmiana_na_czarny()
    else:
        # cv2.imshow("Original", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        image[x, y] = (0, 0, 0)
        (b, g, r) = image[x, y]
        print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

        cv2.imshow("Original", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

zmiana_na_czarny()