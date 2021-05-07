from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from addHwk import mostrar
#from addHwk import openAddHwk
from assets import *
#from addHwk import addHwk

#   hago un objeto mi ventana principal, le mando la ventana
class mainWindow():
    def __init__(self, window):
        self.mainWin = window
        #win.geometry("400x500")
        self.mainWin.title("Homework bro")
        self.mainWin.resizable(False, False) # <- falso en 'x' y en 'y'
        self.mainWin.config(background=mainColor)
        self.mainWin.iconphoto(True, PhotoImage(file="img/windowIcon.png"))
        #                       ^-- Esto significa que se ¿hereda a otras ventanas?

        buttonStyle = ttk.Style()
        buttonStyle.configure(
            "buttonStyle.TButton",
            anchor="n",
            padding=0,
            background=mainColor,
            borderwidth = 0
        )

        logo = Image.open('img/mainImage.png')
        logo = logo.resize((400, 400), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)

        logoLabel = Label(image=logo, borderwidth=0)
        logoLabel.image = logo
        logoLabel.grid(column=0, row=0, rowspan=3)
        
        addHwkImg = Image.open('img/addHwkImage.png')
        addHwkImg = addHwkImg.resize((312, 62), Image.ANTIALIAS)
        addHwkImg = ImageTk.PhotoImage(addHwkImg)

        addHwkButton = ttk.Button(self.mainWin, image=addHwkImg, style="buttonStyle.TButton", command = mostrar)
        addHwkButton.image = addHwkImg
        addHwkButton.grid(column=1, row=0)

        seeHwkImg = Image.open('img/seeHwkImage.png')
        seeHwkImg = seeHwkImg.resize((312, 62), Image.ANTIALIAS)
        seeHwkImg = ImageTk.PhotoImage(seeHwkImg)

        seeHwkButton = ttk.Button(self.mainWin, image=seeHwkImg, style="buttonStyle.TButton")
        seeHwkButton.image = seeHwkImg
        seeHwkButton.grid(column=1, row=1)

        lessHwkImg = Image.open('img/lessHwkImage.png')
        lessHwkImg = lessHwkImg.resize((312, 62), Image.ANTIALIAS)
        lessHwkImg = ImageTk.PhotoImage(lessHwkImg)

        quitHwkButton = ttk.Button(self.mainWin, image=lessHwkImg, style="buttonStyle.TButton")
        quitHwkButton.image = lessHwkImg
        quitHwkButton.grid(column=1, row=2)
        


win = Tk()
application = mainWindow(win)
win.mainloop()