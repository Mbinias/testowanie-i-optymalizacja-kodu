import cv2
image = cv2.imread(r"C:\Users\Student\Downloads\portret-psa-labradora-jako-krola-pupilart.webp")


cv2.namedWindow("Zdjecie", cv2.WINDOW_NORMAL)



cv2.imshow("Zdjecie", image)
cv2.waitKey(0)
cv2.destroyWindow()