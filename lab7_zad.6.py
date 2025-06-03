# 6. Odbicie na podstawie wyboru użytkownika
# a. Napisz skrypt, który wczytuje obraz i pyta użytkownika o sposób odbicia
# ( 0 – pionowe, 1 – poziome, -1 – oba).
# b. Na podstawie wyboru wykonuje operację i wyświetla wynik.

import cv2
image = cv2.imread("zdjecie_psa.png")

while True:
    wybor = int (input("Wybierz sposob odbicia (0 - pionowe, 1 - poziome, -1 - oba): "))
    if wybor in [0, 1, -1]:
        break
    else:
        print("Nieprawidlowy wybor")
flipped = cv2.flip(image, wybor)
cv2.imshow("Flipped ", flipped)

cv2.waitKey(0)