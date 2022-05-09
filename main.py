import pyqrcode
from pyzbar.pyzbar import  decode 
from PIL import Image 
import os

def options():
    print("[1] encode")
    print("[2] decode")
    print("[0] exit the generator ")


def encode():
    qr = pyqrcode.create(str(input("Write here your link to generate a qr for it  : ")))
    to_save = input(" would you like to save the qr? y/n ")
    if to_save == "y": # cant get this part to work
       name = input("What shall the save be called: ")
       if name:
           qr.png(f"{name}.png", scale = 8) 
       else:
           print(" well fuck off, spent time for you to just to not use it ")  

def decode_qr():
        to_save = input("If you are willing to decode your file please y/n: ")

        if to_save == "y":
           name = input("Write the name of your file which you are willing to decode " )

           d = decode(Image.open(f"{name}.png")) 
           print(d[0].data.decode("ascii"))
        else:
            print("Returning to menu...")
        
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
    
def main():
    menu()
        


if __name__ == "__main__":
    main()
     



