# 5. Kadrowanie twarzy
# a. Znajdź zdjęcie z twarzą.
# b. Znajdź obszar, w którym się znajduje, i przytnij obraz tak, aby pozostała
# tylko twarz.

import cv2
import numpy as np

image_path = "Gandalf.jpg"
image = cv2.imread(image_path)
cv2.imshow("Original", image)

startY_face = 30
endY_face = 300
startX_face = 75
endX_face = 185

height, width = image.shape[:2]
if not (0 <= startY_face < endY_face <= height and \
        0 <= startX_face < endX_face <= width):
    print("Wrong coordinates")

face_roi = image[startY_face:endY_face, startX_face:endX_face]

cv2.imshow("Cropped face", face_roi)

cv2.waitKey(0)
cv2.destroyAllWindows()