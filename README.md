# Text to QR Code

## A simple Python script that generates a QR code from user input and displays it using Matplotlib.

### Features
- Generates a QR code from text input
- Uses qrcode library for QR creation
- Displays the QR code using matplotlib.pyplot
- Supports error correction and custom styling

### requirements 
- python
- necessary python libraries
```
pip install pillow matplotlib qrcode
```

### Usage
```
python textToQr.py
```
### example
```
Input text: Hello World
```
- will display this image 

![image](https://github.com/user-attachments/assets/8f1199a4-71a3-4875-b6eb-4f7fbf2ab6b1)

### Customization

The QR code can be modified by adjusting:

- box_size: Size of individual squares in the QR code
- border: Thickness of the border
- error_correction: Level of error correction (L, M, Q, H)
