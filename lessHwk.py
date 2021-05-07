from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from assets import *

def mostrarLess():
    win = Toplevel()
    # No se pueden crear muchas instancias de Tk por que se usa Toplevel
    lessHwk(win)
    win.mainloop()

class lessHwk:
    def __init__(self, window):
        self.lessWindow = window
        self.lessWindow.title("Borrar tarea")
        self.lessWindow.resizable(False, False) # <- falso en 'x' y en 'y'
        self.lessWindow.config(background=mainColor)
        #self.addWindow.iconphoto(False, PhotoImage(file="img/windowIcon.png"))
        self.lessWindow.config( padx = 80)
        
        logoT = Image.open('img/mainImage3.png')
        logoT = logoT.resize((200, 200), Image.ANTIALIAS)
        logoT = ImageTk.PhotoImage(logoT)

        logoLabelAdd = Label(self.lessWindow, image = logoT, borderwidth=0)
        logoLabelAdd.image = logoT
        logoLabelAdd.grid(column=0, row=0)

        lessBtnImg = Image.open('img/lessHwkButton.png')
        lessBtnImg = lessBtnImg.resize((181, 62), Image.ANTIALIAS)
        lessBtnImg = ImageTk.PhotoImage(lessBtnImg)

        quitButton = ttk.Button(self.lessWindow, image=lessBtnImg, style="buttonStyle.TButton")
        quitButton.image = lessBtnImg
        quitButton.grid(column=0, row=2)
    

    
    

