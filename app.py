from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

# <- Colores y fuente ->

mainColor = "#2E4053" # gris
secondaryColor = "#f2f3f4" # blanco con tono ligero de gris
secondaryColor2 = "#5ce1e6" # azul turqueza
secondaryColor3 = "#ffde59" # amarillo
secondaryColor4 = "#7ed957" # verde pasto
secondaryColor5 = "#cb6ce5" # magenta
testColor = "#c8c8c8"

# <- Fuente ->
mainFont = "Raleway"

# <- Objeto de mi ventana principal
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

        logoLabel = Label(self.mainWin, image=logo, borderwidth=0)
        logoLabel.image = logo
        logoLabel.grid(column=0, row=0, rowspan=3)
        
        addHwkImg = Image.open('img/addHwkImage.png')
        addHwkImg = addHwkImg.resize((312, 62), Image.ANTIALIAS)
        addHwkImg = ImageTk.PhotoImage(addHwkImg)

        addHwkButton = ttk.Button(self.mainWin, image=addHwkImg, style="buttonStyle.TButton", command = mostrarAdd)
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

        quitHwkButton = ttk.Button(self.mainWin, image=lessHwkImg, style="buttonStyle.TButton", command = mostrarLess)
        quitHwkButton.image = lessHwkImg
        quitHwkButton.grid(column=1, row=2)

def mostrarAdd():
        win = Toplevel()
        # No se pueden crear muchas instancias de Tk por que se usa Toplevel
        addHwk(win)
        win.mainloop()

class addHwk:
    # Se almacena la base de datos en una variable
    db_name = 'tareas.db'

    def __init__(self, window):
        self.addWindow = window
        self.addWindow.title("Añadir tarea")
        self.addWindow.resizable(False, False) # <- falso en 'x' y en 'y'
        self.addWindow.config(background=mainColor)
        #self.addWindow.iconphoto(False, PhotoImage(file="img/windowIcon.png"))
        self.addWindow.config( padx = 80)
        
        logoT = Image.open('img/mainImage3.png')
        logoT = logoT.resize((200, 200), Image.ANTIALIAS)
        logoT = ImageTk.PhotoImage(logoT)

        logoLabelAdd = Label(self.addWindow, image = logoT, borderwidth=0)
        logoLabelAdd.image = logoT
        logoLabelAdd.grid(column=0, row=0, columnspan = 2)


        Label(self.addWindow, text = "Nombre", bg = mainColor, fg = secondaryColor ,font = (mainColor, 13)).grid(column = 0, row = 1, sticky = W+E, pady = 5)
        self.nombre = Entry(self.addWindow, bg = secondaryColor2 ,relief = "flat", font = (mainFont, 13), justify = "center")
        self.nombre.grid(column = 1, row = 1, sticky = W + E, ipady = 4)  
        self.nombre.focus()

        Label(self.addWindow, text = "Materia", bg = mainColor, fg = secondaryColor ,font = (mainColor, 13)).grid(column = 0, row = 2, sticky = W+E, pady = 5)
        self.materia = Entry(self.addWindow, bg = secondaryColor3 ,relief = "flat", font = (mainFont, 13), justify = "center")
        self.materia.grid(column = 1, row = 2, sticky = W + E, ipady = 4)

        Label(self.addWindow, text = "Descripcion", bg = mainColor, fg = secondaryColor ,font = (mainColor, 13)).grid(column = 0, row = 3, sticky = W+E, pady = 5)
        self.descripcion = Entry(self.addWindow, bg = secondaryColor4 ,relief = "flat", font = (mainFont, 13), justify = "center")
        self.descripcion.grid(column = 1, row = 3, sticky = W + E, ipady = 4)

        Label(self.addWindow, text = "Fecha", bg = mainColor, fg = secondaryColor ,font = (mainColor, 13)).grid(column = 0, row = 4, sticky = W+E, pady = 5)
        self.fecha = Entry(self.addWindow, bg = secondaryColor5 ,relief = "flat", font = (mainFont, 13), justify = "center")
        self.fecha.grid(column = 1, row = 4, sticky = W + E, ipady = 4)

        Label(self.addWindow, text = "Maestro", bg = mainColor, fg = secondaryColor ,font = (mainColor, 13)).grid(column = 0, row = 5, sticky = W+E, pady = 5)
        self.maestro = Entry(self.addWindow, bg = secondaryColor ,relief = "flat", font = (mainFont, 13), justify = "center")
        self.maestro.grid(column = 1, row = 5, sticky = W + E, ipady = 4)

        addBtnImg = Image.open('img/addHwkButton.png')
        addBtnImg = addBtnImg.resize((150, 50), Image.ANTIALIAS)
        addBtnImg = ImageTk.PhotoImage(addBtnImg)

        logoLabelAdd = ttk.Button(self.addWindow, image=addBtnImg, style="buttonStyle.TButton")
        logoLabelAdd.image = addBtnImg
        logoLabelAdd.grid(column=0, row=6, columnspan = 2)

        self.addWindow.grid_columnconfigure(0, weight  = 1)
        self.addWindow.grid_columnconfigure(1, weight  = 2)       
            


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
        lessBtnImg = lessBtnImg.resize((150, 50), Image.ANTIALIAS)
        lessBtnImg = ImageTk.PhotoImage(lessBtnImg)

        quitButton = ttk.Button(self.lessWindow, image=lessBtnImg, style="buttonStyle.TButton")
        quitButton.image = lessBtnImg
        quitButton.grid(column=0, row=2)
    

    
    

win = Tk()
application = mainWindow(win)
win.mainloop()
