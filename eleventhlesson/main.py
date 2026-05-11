import cv2
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files

uploaded = files.upload()
filename = list(uploaded.keys())[0]
print("Загруженный файл:", filename)

image = cv2.imread(filename)

if image is None:
  print("Ошибка")
else:
  print("Изображение успешно загружено")
  print("Размер: ", image.shape)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# plt.figure(figsize=(6,6))
# plt.imshow(image_rgb)
# plt.axis("off")
# plt.title("Original image")
# plt.show()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(
    gray,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)
sobel_y = cv2.Sobel(
    gray,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)
sobel_x_abs = cv2.convertScaleAbs(sobel_x)
sobel_y_abs = cv2.convertScaleAbs(sobel_y)

sobel_combined = cv2.addWeighted(
    sobel_x_abs,
    0.5,
    sobel_y_abs,
    0.5,
    0
)

plt.figure(figsize=(16,10))

plt.subplot(2,2,1)
plt.imshow(image_rgb)
plt.title("Original image")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(gray, cmap = "gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(sobel_x_abs, cmap = "gray")
plt.title("Sobel X: vertical edges")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(sobel_y_abs, cmap = "gray")
plt.title("Sobel Y: horizontal edges")
plt.axis("off")

plt.show()

plt.figure(figsize=(8,8))
plt.imshow(sobel_combined, cmap="gray")
plt.title("Combined Sobel X + Y")
plt.axis("off")
plt.show()