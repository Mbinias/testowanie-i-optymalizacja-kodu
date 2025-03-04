import cv2
image_gray = cv2.imread(r"C:\Users\Student\Downloads\portret-psa-labradora-jako-krola-pupilart.webp", cv2.IMREAD_GRAYSCALE)

cv2.imwrite(r"C:\Users\Student\Downloads\obraz_skalaszarosci.jpg", image_gray)