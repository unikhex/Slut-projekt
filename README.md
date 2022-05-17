# *Qr-code generator and Decoder*

## *Description*

This here is a Qr code generator in which encodes texts or links that it is given and it could also decode already existing qr codes.

## *Language/ Built with*

Python 3.9

Markdown

## *Requirements*

install pyqrcode

install pyzbar

import Image

## *Installation*

Using the Terminal or the Command propmt use pip to install;

 pyqrcode, pyzbar and Image.

The commands used are :

- pip install pyqrcode
- pip install pyzbar
- pip install Image

 First is installing the needed imports from python.
 This is done by writing:

- pip install (name of  the installation)
- i.e pip install pyqrcode
- pip install pyzbar
- pip install Image.

If there is a problem with installing through the terminal,
 open command prompt and do it throught there.

 If there still a problem, check the directory in which pip is, copy that and do it there.

 Example being -- C:\Users\username\AppData\Roaming\Python\scripts
 then there install the needed imports.

## *How it functions*

The code itself  begins by asking you what you will encode/ enccrypt in the Qr-code.

It will then ask you if you would like to save it if the answer is yes,

It will follow up by asking you what name the Qr should be saved as.

It saves it as namegiven.png.

It exists back to the menu.

There will be a choice to decode the qr code that is already there. It asks you to input the name of the Qr. The decryption will then be seen in the terminal.
Image [![image](https://user-images.githubusercontent.com/95760773/168820606-41ef7d5e-cf0c-4fbf-936f-1f780e57b17b.png)
]

## *Changelog for everyversion*

v_1

Nothing much done here
installation of imports

v_1.2

Done with the writing of the code.

The code functions. As in you can encode a link or text behind a picture.

v_1.3

Done with creating a decoder of the qr code.

v_1.4

Most of the time was spent looking for a way to read the name of the qr picture so that i can decode it directly.

V-1.5

Started created the menu and fuctions in which the decode and encoder were in

v_1.6

Creating a better system for the saves and calling the saves back to the decoder.

v_1.7

Too much was being shown in the terminal when i asked the decoder to ddecode.

Fixing this was was attaching (ascii) to the data.decode.

v_1.8

Done with the menu, functions, the save and the calling back the saves.

## *What was removed*

removed a global that made my code. Made it buggy

Had functions for decoding but they didnt work so they were removes.

I was importing the os, this was removed since i icluded a menu option that if you exit it takes you directly back to the beginning.

## *Problems that I had*

in v_1.8

There was a bug that you couldnt start the proess since you couldnt input anything.

- It was fixed by deleting one input since  i had tw inputs in the same place asking the same thing.

Had a problem with saving the Qr as the input name that the person chooses themselves.

- It was solved by the help of Shazoud who gave me the idea of using an f string instead of calling back to the variable directly.

Biggest problem was wondering how a menu should look like.

- Was solved by the help of my teacher Niclas who had a whole video on specificly this.

## *License*

[MIT](https://choosealicense.com/licenses/mit/)

## *Contact*

Zion Awino (unikhex )

- [Email] (awinozion85@gmail.com)
- [Project_link] (<https://github.com/unikhex/Slut-projekt>)

## *Acknowledgements*

Credit to:

- Niclas
[Email](niclas.lund@ga.ntig.se)
- Shazhoud
[Email](shahzod.ravshanov@elev.ga.ntig.se )
