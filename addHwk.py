from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from assets import *

class addHwkWindow():
    def __init__(self, window):
        self.addWindow = window
        self.addWindow.geometry("500x500")
        self.addWindow.title("Añadir tarea")
        #self.addWindow.resizable(False, False) # <- falso en 'x' y en 'y'
        self.addWindow.config(background=mainColor)
        self.addWindow.iconphoto(True, PhotoImage(file="img/windowIcon.png"))
        
        

        Label(self.addWindow, text = "Nombre", bg = secondaryColor2, font = mainColor, justify = "left").grid(column = 0, row = 0, sticky = W+E)
        self.name = Entry(self.addWindow, bg = secondaryColor,relief = "flat", font = mainFont)
        self.name.grid(column = 1, row = 0, sticky = W + E)
        #Label(self.addWindow, text = "Nombre", bg = secondaryColor3, font = mainColor)

        self.addWindow.grid_columnconfigure(0, weight  = 2)
        self.addWindow.grid_columnconfigure(1, weight  = 2)

        self.addWindow.grid_rowconfigure(0, weight  = 2)
        self.addWindow.grid_rowconfigure(1, weight  = 2)






win = Tk()
addHwk = addHwkWindow(win)
win.mainloop()
