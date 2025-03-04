import cv2

image = cv2.imread(r"C:\Users\Student\Downloads\portret-psa-labradora-jako-krola-pupilart.webp")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")