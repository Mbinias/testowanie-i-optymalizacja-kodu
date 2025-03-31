import cv2

image = cv2.imread('zdjecie_psa.png')

pixel1 = image[50, 50]
pixel2 = image[200, 200]

print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(pixel1[2], pixel1[1], pixel1[0]))
print("Pixel at (200, 200) - Red: {}, Green: {}, Blue: {}".format(pixel2[2], pixel2[1], pixel2[0]))

diff_b = int(pixel2[0]) - int(pixel1[0])
diff_g = int(pixel2[1]) - int(pixel1[1])
diff_r = int(pixel2[2]) - int(pixel1[2])

print("Różnica wartości - Red: {}, Green: {}, Blue: {}".format(diff_r, diff_g, diff_b))
