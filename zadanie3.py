import cv2
image_gray = cv2.imread(r"C:\Users\Student\Downloads\portret-psa-labradora-jako-krola-pupilart.webp", cv2.IMREAD_GRAYSCALE)

if len(image_gray.shape) == 2:
    channels = 1
else:
    channels = image_gray.shape[2]

print(f'channels: {channels}')
cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()