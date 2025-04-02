
from PIL import Image
import matplotlib.pyplot as plt
import qrcode

input = input("Input text: ")

qr = qrcode.QRCode(
    version=1, #version
    error_correction=qrcode.constants.ERROR_CORRECT_L, #error correction
    box_size=10, #size of each box in QR
    border=4, #border thickness
    )


image = Image.open("image.jpg")

plt.imshow(image)
plt.axis('off')
plt.show()
