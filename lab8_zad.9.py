# 9. Zapis przyciętego obrazu
# a. Przytnij obraz do obszaru o wymiarach 300x300 pikseli.
# b. Zapisz wynik jako nowy plik cropped_image.jpg .

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original Image", image)

crop_startX = 50
crop_startY = 50
crop_width = 300
crop_height = 300

crop_endX = crop_startX + crop_width
crop_endY = crop_startY + crop_height

image_height, image_width = image.shape[:2]
if crop_endX > image_width:
    crop_endX = image_width
if crop_endY > image_height:
    crop_endY = image_height

cropped_image = image[crop_startY:crop_endY, crop_startX:crop_endX]

cv2.imshow("Cropped Image", cropped_image)

cv2.imwrite("cropped_image.jpg", cropped_image)
print("\nCropped image successfully saved as 'cropped_image.jpg'")

cv2.waitKey(0)
cv2.destroyAllWindows()