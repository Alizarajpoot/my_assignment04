
#project 3 qrcode generator

import qrcode
from PIL import Image
from IPython.display import display

# QR Code Data
data = "Generate QR code using make() function"

# Create QR Code
qr_img = qrcode.make(data)

# Save the QR Code
qr_img.save("qr.png")

# Open and Display the QR Code (Only for Jupyter Notebook)
img = Image.open("qr.png")
display(img)

print("✅ QR Code generated and saved as 'qr.png'!")
