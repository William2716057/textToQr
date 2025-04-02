
from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("image.jpg")

plt.imshow(image)
plt.axis('off')
plt.show()
