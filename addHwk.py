from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from assets import *

def mostrarAdd():
    win = Toplevel()
    # No se pueden crear muchas instancias de Tk por que se usa Toplevel
    addHwk(win)
    win.mainloop()

class addHwk:
    def __init__(self, window):
        self.addWindow = window
        self.addWindow.title("Añadir tarea")
        self.addWindow.resizable(False, False) # <- falso en 'x' y en 'y'
        self.addWindow.config(background=mainColor)
        #self.addWindow.iconphoto(False, PhotoImage(file="img/windowIcon.png"))
        self.addWindow.config( padx = 80)
        
        def linea(self, titulo, colorEntrada, renglon):
            Label(self.addWindow, text = titulo, bg = mainColor, fg = secondaryColor ,font = (mainColor, 13)).grid(column = 0, row = renglon, sticky = W+E, pady = 5)
            self.name = Entry(self.addWindow, bg = colorEntrada ,relief = "flat", font = (mainFont, 13), justify = "center")
            self.name.grid(column = 1, row = renglon, sticky = W + E, ipady = 4)
        
        logoT = Image.open('img/mainImage3.png')
        logoT = logoT.resize((200, 200), Image.ANTIALIAS)
        logoT = ImageTk.PhotoImage(logoT)

        logoLabelAdd = Label(self.addWindow, image = logoT, borderwidth=0)
        logoLabelAdd.image = logoT
        logoLabelAdd.grid(column=0, row=0, columnspan = 2)

        linea(self, titulo="Nombre", colorEntrada=secondaryColor2, renglon=1)
        linea(self, titulo="Materia", colorEntrada=secondaryColor3, renglon=2)
        linea(self, titulo="Descripcion", colorEntrada=secondaryColor4, renglon=3)
        linea(self, titulo="Fecha", colorEntrada=secondaryColor5, renglon=4)
        linea(self, titulo="Maestro", colorEntrada = secondaryColor, renglon = 5)      
        
        self.addWindow.grid_columnconfigure(0, weight  = 1)
        self.addWindow.grid_columnconfigure(1, weight  = 2)


#mostrar()