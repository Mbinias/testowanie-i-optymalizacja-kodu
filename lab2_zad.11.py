import cv2

image = cv2.imread('zdjecie_psa.png')

(h, w, _) = image.shape

max_brightness = 0
max_loc = (0, 0)

for y in range(h):
    for x in range(w):
        b, g, r = image[y, x]
        brightness = (int(b) + int(g) + int(r)) / 3
        if brightness > max_brightness:
            max_brightness = brightness
            max_loc = (x, y)

print("Najjaśniejszy piksel znajduje się w:", max_loc, "z wartością jasności:", max_brightness)
