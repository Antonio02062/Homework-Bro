from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from addHwk import openAddHwk
from assets import *
#from addHwk import addHwk

win = Tk()
win.title("Homework bro")
#win.geometry("400x500")
win.resizable(False, False)  # <- falso en 'x' y en 'y'
win.config(background=mainColor)
win.iconphoto(True, PhotoImage(file='img/windowIcon.png'))
#              ^-- Esto significa que se ¿hereda a otras ventanas?

# logo
logo = Image.open('img/mainImage.png')
logo = logo.resize((500, 500), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

logoLabel = Label(image=logo, borderwidth=0)
logoLabel.image = logo
logoLabel.grid(column=0, row=0, rowspan=3)


buttonStyle = ttk.Style()
buttonStyle.configure(
    "buttonStyle.TButton",
    anchor="n",
    padding=0,
    background=mainColor,
    borderwidth = 0
)

addHwkImg = Image.open('img/addHwkImage.png')
addHwkImg = addHwkImg.resize((312, 62), Image.ANTIALIAS)
addHwkImg = ImageTk.PhotoImage(addHwkImg)

addHwkButton = ttk.Button(win, image=addHwkImg, style="buttonStyle.TButton", command = openAddHwk)
addHwkButton.grid(column=1, row=0)

seeHwkImg = Image.open('img/seeHwkImage.png')
seeHwkImg = seeHwkImg.resize((312, 62), Image.ANTIALIAS)
seeHwkImg = ImageTk.PhotoImage(seeHwkImg)

seeHwkButton = ttk.Button(win, image=seeHwkImg, style="buttonStyle.TButton")
seeHwkButton.grid(column=1, row=1)

lessHwkImg = Image.open('img/lessHwkImage.png')
lessHwkImg = lessHwkImg.resize((312, 62), Image.ANTIALIAS)
lessHwkImg = ImageTk.PhotoImage(lessHwkImg)

quitHwkButton = ttk.Button(win, image=lessHwkImg, style="buttonStyle.TButton")
quitHwkButton.grid(column=1, row=2)

win.mainloop()

