import pyqrcode
from pyzbar.pyzbar import  decode
from PIL import Image

qr = pyqrcode.create("First try lets see if it worked")
qr.png("letsgo.png", scale = 8)

d = decode (image.open("letsgo.png"))
print(d[0].data.decode("ascii"))