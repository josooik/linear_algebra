# 이미지 출력
import cv2
import matplotlib
import matplotlib.pyplot as plt
print(cv2.__version__)

img_src = cv2.imread('img/image.jpg', cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_src, cv2.COLOR_BGR2RGB)

dpi = matplotlib.rcParams['figure.dpi']

height, width = img_src.shape[:2]
figsize = width / float(dpi), height / float(dpi)
plt.figure(figsize=figsize)

plt.imshow(img_rgb)
plt.title('animal')
plt.axis('off')
plt.show()

