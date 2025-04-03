
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

#add input text to QR code
qr.add_data(input)
qr.make(fit=True)

#create image of QR
image = qr.make_image(fill="black", back_color="white")
#image.save("image.jpg")
#image = Image.open("image.jpg")

plt.imshow(image)
plt.axis('off')
plt.show()
