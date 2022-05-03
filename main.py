import pyqrcode #was easiliy installed using pip now just import
from pyzbar.pyzbar import  decode # the decoder used to decode the qr code above
from PIL import Image #changes the qr code that i have to an image that is saved else where

qr = pyqrcode.create(str(input("Write here your link : ")))
qr.png("letsgo.png", scale = 8)

d = decode (Image.open("letsgo.png"))# had a problem with the image
# didnt know that without capital letter I it wont work had to look for a couple of minutes what the fuck was wrong with this code
print(d[0].data.decode("ascii"))