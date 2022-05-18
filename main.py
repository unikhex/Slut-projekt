import pyqrcode
from pyzbar.pyzbar import  decode 
from PIL import Image 

# imports that are needed for the code to work
#pyqrcode is what makes it possible to easily created qr.codes without needing to do much
#From pyzbar we import decode to decode. This makes it possible to decode the qr codes.
#IMage makes it possible to save the qr ocdes as an image file, such as .png, jpeg,jpg and many more.

def options():
    print("\n\nWelcome to Thee Qr code generator and decoder\n")

    print("[1] encode")
    print("[2] decode")
    print("[0] exit the generator ")
#We define some options that we will put in the menu later
# One is to encode
# the second to decode
# and the last is to exit the code


def encode():
    print("\n Welcome to the encoder.\n")

    qr = pyqrcode.create(str(input("Write here your link to generate a qr for it  : ")))
    to_save = input("\n Would you like to save the qr? y/n \n")
    if to_save == "y": # cant get this part to work
       name = input("\n What shall the save be called:\n ")
       if name:
           qr.png(f"{name}.png", scale = 8) 
    elif to_save == "n":
        print(" Well fuck off i spent so much time on this for you to just not use it")
    else:
           print("Returning to menu...")  
    
    ''' The function creates a qr code, ask for an input on the name the qr should dbe saved as, 
    then saves the Qr as the namegiven.png 
    If the person choses no to svae it just returns to the menu and the process repeats.
    '''       

# The above function first creates a qr code with a link/text that you give it with the variable qr.
#Then you are asked if you would like to save the qr 
#It then saves the qr.code as the name that was given by you.
#If you chose not to save it will just return you to the menu.

def decode_qr():
        print("\n Welcome to the decoder.\n")
        to_save = input("\n Are you here to decode your file please y/n: \n ")

        if to_save == "y":
           name = input("\n Write the name of the file you want to decode \n" )

           d = decode(Image.open(f"{name}.png")) 
           print(d[0].data.decode("ascii"))
        else:
            print("Returning to menu...")
    
        ''' The above function asks for a name of a saved qr code,
         decrypts the message/ link behind that qr code,
         It uses the Import Image to decrypt the picture of the Qr with the name that waas given,
          it then displays the message that we need which is the [0] in the terminal.
          Everything else is irrelevant as in without the [0] and ascii it would display everything including the size of the picture 
          and all that we dont need those.
        '''
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
        if choice == "1":
            encode()
        if choice == "2":
            decode_qr()
        elif choice == "decode":
            decode_qr()
        elif choice == "0":
            break

        options()
        choice = input(">> ")
    else:
        print(" You chose fuck off, good")
    '''It calls back to the the function we defined ealier(options),
    Inputting "0" or something will automaticly break the code
    The first choice is encode. This allows you to create a Qr
    The second choice is decode, it decrypts the Qr and displays the message/ link behind it.

    '''
#We begin by calling back the options that we defined earlier.
#We then bring up choices, you can either chose from choice one (encode),or choice 2 (decode)
#Anything else will bring you back to  the menu. Since if anything else is there the code breaks.
    
def main():
    menu()
        

if __name__ == "__main__":
    main()
     



