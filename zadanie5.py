import cv2
image = cv2.imread(r"C:\Users\Student\Downloads\portret-psa-labradora-jako-krola-pupilart.webp")
cv2.imshow("Zdjecie1", image)
cv2.imshow("Zdjecie2", image)

cv2.waitKey(0)
cv2.destroyWindow("Zdjecie1")
cv2.waitKey(0)
cv2.destroyWindow("Zdjecie1")
