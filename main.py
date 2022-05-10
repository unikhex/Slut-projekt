import pyqrcode
from pyzbar.pyzbar import  decode 
from PIL import Image 
import os
# imports that are needed for the code to work
#pyqrcode is what makes it possible to easily created qr.codes without needing to do much
#From pyzbar we import decode to decode. This makes it possible to decode the qr codes.
#IMage makes it possible to save the qr ocdes as an image file, such as .png, jpeg,jpg and many more.


def options():
    print("[1] encode")
    print("[2] decode")
    print("[0] exit the generator ")
#We define some options that we will put in the menu later
# One is to encode
# the second to decode
# and the last is to exit the code


def encode():
    print("Welcome to the QR code generator.")

    qr = pyqrcode.create(str(input("Write here your link to generate a qr for it  : ")))
    to_save = input(" Would you like to save the qr? y/n ")
    if to_save == "y": # cant get this part to work
       name = input("What shall the save be called: ")
       if name:
           qr.png(f"{name}.png", scale = 8) 
    elif to_save == "n":
        print(" Well fuck off i spent so much time on this for you to just not use it")
    else:
           print("Returning to menu...")  
# The above function first creates a qr code with a link/text that you give it with the variable qr.
#Then you are asked if you would like to save the qr 
#It then saves the qr.code as the name that was given by you.
#If you chose not to save it will just return you to the menu.

def decode_qr():
        to_save = input("If you are willing to decode your file please y/n: ")

        if to_save == "y":
           name = input("Write the name of your file which you are willing to decode " )

           d = decode(Image.open(f"{name}.png")) 
           print(d[0].data.decode("ascii"))
        else:
            print("Returning to menu...")
# The function is basicly the same as the encode one,
#  It asks for an input if you would like to decode a saved qr code
# If choice is yes it will ask for the name of the of the qr code then it will deocde it
# else if you dont want to decode it it will just return you to the menu        
        
def menu():
    options()
    choice = input(">>")
    
    while choice != "0":
        
        if choice == "encode":
            encode()
        elif choice == "decode":
            decode_qr()
        elif choice == "0":
            break

        options()
        choice = input(">> ")
    else:
        print(" You chose fuck off, good")
#We begin by calling back the options that we defined earlier.
#We then bring up choices, you can either chose from choice one (encode),or choice 2 (decode)
#Anything else will bring you back to  the menu. Since if anything else is there the code breaks.
    
def main():
    menu()
        

if __name__ == "__main__":
    main()
     



