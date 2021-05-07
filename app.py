from tkinter import *
from tkinter import ttk , messagebox
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
        logoLabel.grid(column=0, row=0, rowspan=2)
        
        addHwkImg = Image.open('img/addHwkImage.png')
        addHwkImg = addHwkImg.resize((312, 62), Image.ANTIALIAS)
        addHwkImg = ImageTk.PhotoImage(addHwkImg)

        addHwkButton = ttk.Button(self.mainWin, image=addHwkImg, style="buttonStyle.TButton", command = mostrarAdd)
        addHwkButton.image = addHwkImg
        addHwkButton.grid(column=1, row=0, padx = 40)

        lessHwkImg = Image.open('img/lessHwkImage.png')
        lessHwkImg = lessHwkImg.resize((312, 62), Image.ANTIALIAS)
        lessHwkImg = ImageTk.PhotoImage(lessHwkImg)

        quitHwkButton = ttk.Button(self.mainWin, image=lessHwkImg, style="buttonStyle.TButton", command = mostrarLess)
        quitHwkButton.image = lessHwkImg
        quitHwkButton.grid(column=1, row=1)

def mostrarAdd():
        win = Toplevel()
        # No se pueden crear muchas instancias de Tk por que se usa Toplevel
        addHwk(win)
        win.mainloop()

class addHwk:
    # Se almacena la base de datos en una variable
    
    def __init__(self, window):
        self.db_name = 'tareas.db'
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

        logoLabelAdd = ttk.Button(self.addWindow, image=addBtnImg, style="buttonStyle.TButton", command = self.add_tareas)
        logoLabelAdd.image = addBtnImg
        logoLabelAdd.grid(column=0, row=6, columnspan = 2, pady = 20)

        self.addWindow.grid_columnconfigure(0, weight  = 1)
        self.addWindow.grid_columnconfigure(1, weight  = 2)

    # método que hace la conexión a la base de datos
    # cada vez que se quiera hacer una acción con la misma
    def run_query(self, query, parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parametros)
            conn.commit()
        return resultado

    # Validar que todos los campos tengan informacion
    def validation(self):
        return (len(self.nombre.get()) != 0 and len(self.materia.get()) != 0 and len(self.maestro.get()) != 0 and
                len(self.descripcion.get()) != 0 and len(self.fecha.get()) != 0)

    # Añade las tareas a la base de datos
    def add_tareas(self):
        if self.validation():
            query = 'INSERT INTO tareas VALUES(NULL, ?, ? , ?, ?, ?)'
            parametros=(self.nombre.get(), self.materia.get(), self.maestro.get(),
                        self.descripcion.get(), self.fecha.get())
            self.run_query(query, parametros)
            #self.message['text'] = 'La tarea ha sido añadido de manera exitosa'
            messagebox.showinfo(title="Bien!", message="La La tarea ha sido añadido de manera exitosa")
            # Limpia los entry
            self.nombre.delete(0, END)
            self.materia.delete(0, END)
            self.maestro.delete(0, END)
            self.descripcion.delete(0, END)
            self.fecha.delete(0, END)
        
        else:
            messagebox.showinfo(title="Hey!", message="Por favor no dejes ningún campo en blanco")       
        
        self.get_tareas()
    
    def get_tareas(self):
        # Se limpia la tabla
        """records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)"""
        # Se consutan los datos
        query = 'SELECT * FROM tareas ORDER BY id ASC'
        self.run_query(query)
        # Se rellenan los datos
        """for row in db_rows:
            self.tree.insert('', '0', text=(row[1]), values=(row[2], row[3], row[4], row[5]))"""

def mostrarLess():
    win = Toplevel()
    # No se pueden crear muchas instancias de Tk por que se usa Toplevel
    lessHwk(win)
    win.mainloop()

class lessHwk:

    def __init__(self, window):
        self.db_name = 'tareas.db'
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
        logoLabelAdd.grid(column=0, row=0, columnspan = 2)

        lessBtnImg = Image.open('img/lessHwkButton.png')
        lessBtnImg = lessBtnImg.resize((150, 50), Image.ANTIALIAS)
        lessBtnImg = ImageTk.PhotoImage(lessBtnImg)

        quitButton = ttk.Button(self.lessWindow, image=lessBtnImg, command = self.borrar_tarea)
        quitButton.image = lessBtnImg
        quitButton.grid(column=0, row=11, columnspan = 2, pady = 20)

        self.tree = ttk.Treeview(self.lessWindow, height=10, columns=('#1', '#2', '#3', '#4'))
        self.tree.grid(column=0, row=10, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Materia', anchor=CENTER)
        self.tree.heading('#2', text='Maestro', anchor=CENTER)
        self.tree.heading('#3', text='Descripción', anchor=CENTER)
        self.tree.heading('#4', text='Fecha', anchor=CENTER)

        self.get_tareas()
        # método que hace la conexión a la base de datos
        # cada vez que se quiera hacer una acción con la misma
    def run_query(self, query, parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parametros)
            conn.commit()
        return resultado
    
    def get_tareas(self):
        # Se limpia la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Se consutan los datos
        query = 'SELECT * FROM tareas ORDER BY id ASC'
        db_rows = self.run_query(query)
        # Se rellenan los datos
        for row in db_rows:
            self.tree.insert('', '0', text=(row[1]), values=(row[2], row[3], row[4], row[5]))
    
    # Borrar una tarea seleccionada
    def borrar_tarea(self):
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError:
            messagebox.showinfo(title="Hey!", message="¿Que quieres elimininar?") 
            return
        nombre = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM tareas WHERE nombre = ?'
        self.run_query(query, (nombre, ))
        messagebox.showinfo(title="Ojo!", message="La tarea ha sido borrada!") 
        self.get_tareas()


win = Tk()
application = mainWindow(win)
win.mainloop()
