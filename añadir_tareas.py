import tkinter as tk
import tkinter.messagebox


class Tarea:
    def __init__(self, name, ma, mtro, des, fe):
        self.__nombre = name
        self.__materia = ma
        self.__maestro = mtro
        self.__descripcion = des
        self.__fecha = fe

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, n):
        self.__nombre = n

    def get_materia(self):
        return self.__materia

    def set_materia(self, m):
        self.__materia = m

    def get_maestro(self):
        return self.__maestro

    def set_maestro(self, mtro):
        self.__maestro = mtro

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, des):
        self.__descripcion = des

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fe):
        self.__fecha = fe


def add():
    tarea1 = Tarea(nombre, materia, maestro, descripcion, fecha)
    print(f"{tarea1.get_nombre()}")
    print(f"{nombre.get()} \n"
          f"{materia.get()} \n"
          f"{maestro.get()} \n"
          f"{descripcion.get()} \n"
          f"{fecha.get()} \n")


# colores
mainColor = "#2E4053" # gris
secondaryColor = "#f2f3f4" # blanco con tono ligero de gris
secondaryColor2 = "#5ce1e6" # azul turqueza
secondaryColor3 = "#ffde59" # amarillo
secondaryColor4 = "#7ed957" # verde pasto
secondaryColor5 = "#cb6ce5" # magenta
testColor = "#c8c8c8"

# fuentes
mainFont = "Raleway"

# se crea la ventana principal del programa
win = tk.Tk()
win.title("Tarea Nueva")
win.geometry("320x200")
win.configure(bg=mainColor)

# etiquetas
nombre_label = tk.Label(win, bg=mainColor, fg=secondaryColor2, font=(mainFont, 18), text="Nombre: ")
nombre_label.grid(column=1, row=0, sticky = "e")

materia_label = tk.Label(win, bg=mainColor, fg=secondaryColor2, font=(mainFont, 18), text="Materia: ")
materia_label.grid(column=1, row=1, sticky = "e")

maestro_label = tk.Label(win, bg=mainColor, fg=secondaryColor2, font=(mainFont, 18), text="Maestro: ")
maestro_label.grid(column=1, row=2, sticky = "e")

des_label = tk.Label(win, bg=mainColor, fg=secondaryColor2, font=(mainFont, 18),  text="Descripción: ")
des_label.grid(column=1, row=3, sticky = "e")

fecha_label = tk.Label(win, bg=mainColor, fg=secondaryColor2, font=(mainFont, 18),  text="Fecha: ")
fecha_label.grid(column=1, row=4, sticky = "e")


# entradas de las etiquetas
nombre = tk.StringVar()
nombre_entry = tk.Entry(win, bg=secondaryColor, textvariable=nombre)
nombre_entry.grid(column=2, row=0)

materia = tk.StringVar()
materia_entry = tk.Entry(win, textvariable=materia)
materia_entry.grid(column=2, row=1)

maestro = tk.StringVar()
maestro_entry = tk.Entry(win, textvariable=maestro)
maestro_entry.grid(column=2, row=2)

descripcion = tk.StringVar()
des_entry = tk.Entry(win, textvariable=descripcion)
des_entry.grid(column=2, row=3)

fecha = tk.StringVar()
fecha_entry = tk.Entry(win, textvariable=fecha)
fecha_entry.grid(column=2, row=4)

boton_add = tk.Button(win, bg=secondaryColor5, fg=secondaryColor, font=(mainFont, 12), text="Añadir", command=add)
boton_add.grid(column=1, row=5)
boton_Salir = tk.Button(win, bg=secondaryColor2, fg=secondaryColor, font=(mainFont, 12), text="Cerrar", command=win.destroy)
boton_Salir.grid(column=2, row=5)

win.mainloop()
