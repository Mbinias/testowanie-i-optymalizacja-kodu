# 5. Porównanie skuteczności redukcji szumów
# a. Dodaj do obrazu sztuczny szum (np. cv2.randn() do dodania szumu Gaussa
# lub cv2.randu() do szumu soli i pieprzu)
# b. Następnie zastosuj różne metody rozmycia i oceń, która najlepiej usuwa
# szum, zachowując detale obrazu.

import cv2
import numpy as np

image_path = "zdjecie_psa.png"
image = cv2.imread(image_path)
cv2.imshow("Original Image", image)
cv2.waitKey(0)

noise_gaussian = np.zeros(image.shape, np.int16)
cv2.randn(noise_gaussian, 0, 50)
noisy_gaussian_image = cv2.add(image.astype(np.int16), noise_gaussian)
noisy_gaussian_image = np.clip(noisy_gaussian_image, 0, 255).astype(np.uint8)
cv2.imshow("Image with Gaussian Noise", noisy_gaussian_image)
cv2.waitKey(0)

noisy_salt_pepper_image = image.copy()
salt_vs_pepper = 0.5
amount = 0.04
num_salt = np.ceil(amount * image.size * salt_vs_pepper)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in noisy_salt_pepper_image.shape]
noisy_salt_pepper_image[coords[0], coords[1], :] = 255

num_pepper = np.ceil(amount * image.size * (1.0 - salt_vs_pepper))
coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in noisy_salt_pepper_image.shape]
noisy_salt_pepper_image[coords[0], coords[1], :] = 0
cv2.imshow("Image with Salt & Pepper Noise", noisy_salt_pepper_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

blurred_avg_gaussian = cv2.blur(noisy_gaussian_image, (5, 5))
cv2.imshow("Avg Blur (Gaussian Noise)", blurred_avg_gaussian)
cv2.waitKey(0)

blurred_gaussian_gaussian = cv2.GaussianBlur(noisy_gaussian_image, (5, 5), 0)
cv2.imshow("Gaussian Blur (Gaussian Noise)", blurred_gaussian_gaussian)
cv2.waitKey(0)

blurred_median_gaussian = cv2.medianBlur(noisy_gaussian_image, 5)
cv2.imshow("Median Blur (Gaussian Noise)", blurred_median_gaussian)
cv2.waitKey(0)

blurred_bilateral_gaussian = cv2.bilateralFilter(noisy_gaussian_image, 9, 75, 75)
cv2.imshow("Bilateral (Gaussian Noise)", blurred_bilateral_gaussian)
cv2.waitKey(0)

cv2.destroyAllWindows()

blurred_avg_sp = cv2.blur(noisy_salt_pepper_image, (5, 5))
cv2.imshow("Avg Blur (S&P Noise)", blurred_avg_sp)
cv2.waitKey(0)

blurred_gaussian_sp = cv2.GaussianBlur(noisy_salt_pepper_image, (5, 5), 0)
cv2.imshow("Gaussian Blur (S&P Noise)", blurred_gaussian_sp)
cv2.waitKey(0)

blurred_median_sp = cv2.medianBlur(noisy_salt_pepper_image, 5)
cv2.imshow("Median Blur (S&P Noise)", blurred_median_sp)
cv2.waitKey(0)

blurred_bilateral_sp = cv2.bilateralFilter(noisy_salt_pepper_image, 9, 75, 75)
cv2.imshow("Bilateral (S&P Noise)", blurred_bilateral_sp)
cv2.waitKey(0)

cv2.destroyAllWindows()

#Szum Gaussa: Najlepiej redukuje cv2.GaussianBlur i cv2.bilateralFilter
#Szum soli i pieprzu: Najskuteczniejszy jest cv2.medianBlur
# Zachowanie detali: cv2.bilateralFilter najlepiej usuwa szum, zachowując krawędzie