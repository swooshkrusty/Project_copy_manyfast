# import pyzbar.pyzbar

# print(pyzbar.pyzbar.__file__)
# import pyzbar

# print(pyzbar.__version__)

# import sys

# print(sys.path)

import pyzbar

print(pyzbar.__version__)

from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol

img = Image.open("data/src/barcode_qrcode.jpg")

decoded_list = decode(img)

print(type(decoded_list))
