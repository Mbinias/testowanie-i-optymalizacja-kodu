# 6. Symulacja efektu głębi ostrości (dobrze znana fraza w fotografii, jeśli jej nie
# znasz, to zrób research)
# a. Wybierz zdjęcie z obiektami w różnych odległościach od aparatu.
# b. Spróbuj zasymulować efekt głębi ostrości, rozmywając tylko tło, a
# pozostawiając główny obiekt wyraźny.
# c. Możesz zrobić to, ręcznie maskując obszar tła i stosując cv2.GaussianBlur
# tylko na nim.

import cv2
import numpy as np

image_path = "zdjecie_psa.png"

image = cv2.imread(image_path)

cv2.imshow("Original Image", image)
cv2.waitKey(0)

mask_background = np.zeros(image.shape[:2], dtype="uint8")

object_x1, object_y1 = 300, 150
object_x2, object_y2 = 500, 450

mask_background = np.ones(image.shape[:2], dtype="uint8") * 255
cv2.rectangle(mask_background, (object_x1, object_y1), (object_x2, object_y2), 0, -1)

cv2.imshow("Background Mask (White is blurred, Black is sharp)", mask_background)
cv2.waitKey(0)

blurred_background = cv2.GaussianBlur(image, (45, 45), 0)
cv2.imshow("Fully Blurred Image", blurred_background)
cv2.waitKey(0)

background_only = cv2.bitwise_and(blurred_background, blurred_background, mask=mask_background)
cv2.imshow("Blurred Background Only", background_only)
cv2.waitKey(0)

foreground_mask = cv2.bitwise_not(mask_background)
foreground_only = cv2.bitwise_and(image, image, mask=foreground_mask)
cv2.imshow("Sharp Foreground Only", foreground_only)
cv2.waitKey(0)

final_image_dof = cv2.add(background_only, foreground_only)
cv2.imshow("Simulated Depth of Field", final_image_dof)

cv2.waitKey(0)
cv2.destroyAllWindows()