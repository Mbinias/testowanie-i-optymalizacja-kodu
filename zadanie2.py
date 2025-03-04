import cv2


image = cv2.imread(r"C:\Users\Student\Downloads\portret-psa-labradora-jako-krola-pupilart.webp")
(h, w, c) = image.shape[:3]
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')