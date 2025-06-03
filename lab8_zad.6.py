# 6. Kopiowanie i wklejanie fragmentu obrazu
# a. Przytnij określony fragment obrazu (np. o wymiarach 100x100 pikseli).
# b. Wklej ten fragment w inne miejsce na obrazie.

import cv2
import numpy as np

image = cv2.imread("zdjecie_psa.png")
cv2.imshow("Original Image", image)

crop_startX = 100
crop_startY = 50
crop_width = 100
crop_height = 100

crop_endX = crop_startX + crop_width
crop_endY = crop_startY + crop_height

image_height, image_width = image.shape[:2]
if crop_endX > image_width:
    crop_endX = image_width
if crop_endY > image_height:
    crop_endY = image_height

roi = image[crop_startY:crop_endY, crop_startX:crop_endX]

paste_startX = 250
paste_startY = 150

paste_endX = paste_startX + roi.shape[1]
paste_endY = paste_startY + roi.shape[0]

if paste_endX > image_width:
    paste_endX = image_width
if paste_endY > image_height:
    paste_endY = image_height

effective_roi = roi[0:(paste_endY - paste_startY), 0:(paste_endX - paste_startX)]

output_image = image.copy()

output_image[paste_startY:paste_endY, paste_startX:paste_endX] = effective_roi

cv2.imshow("Image with Pasted ROI", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()