import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
# import tkinter.messagebox


class Tarea:
    # Se almacena la base de datos en una variable
    db_name = 'tareas.db'

    def __init__(self, window):
        # Colores
        mainColor = "#2E4053"  # gris
        secondaryColor = "#f2f3f4"  # blanco con tono ligero de gris
        secondaryColor2 = "#5ce1e6"  # azul turqueza
        secondaryColor3 = "#ffde59"  # amarillo
        secondaryColor4 = "#7ed957"  # verde pasto
        secondaryColor5 = "#cb6ce5"  # magenta
        testColor = "#c8c8c8"

        # Fuentes
        mainFont = "Raleway"

        # Initializations
        self.wind = window
        self.wind.title('Añadir Tareas')
        self.wind.configure(bg=mainColor)

        # Se crea un nuevo frame
        frame = LabelFrame(self.wind, text='Añadir una nueva tarea')
        frame.grid(column=0, row=0, columnspan=3, pady=20)

        # Nombre Input
        Label(frame, text='Nombre: ').grid(column=0, row=1)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(column=1, row=1)

        # Materia Input
        Label(frame, text='Materia: ').grid(column=0, row=2)
        self.materia = Entry(frame)
        self.materia.grid(column=1, row=2)

        # Maestro Input
        Label(frame, text='Maestro: ').grid(column=0, row=3)
        self.maestro = Entry(frame)
        self.maestro.grid(column=1, row=3)

        # Descripcion Input
        Label(frame, text='Descripción: ').grid(column=0, row=4)
        self.descripcion = Entry(frame)
        self.descripcion.grid(column=1, row=4)

        # Fecha Input
        Label(frame, text='Fecha: ').grid(column=0, row=5)
        self.fecha = Entry(frame)
        self.fecha.grid(column=1, row=5)

        # Boton añadir/get/salir
        ttk.Button(frame, text='Añadir Tarea', command=self.add_tareas).grid(columnspan=2, row=7, sticky=W + E)
        ttk.Button(frame, text='Ver Tareas', command=self.get_tareas).grid(columnspan=2, row=8, sticky=W + E)
        ttk.Button(frame, text='Salir', command=self.wind.destroy).grid(columnspan=2, row=9, sticky=W + E)

        # Boton Borrar
        ttk.Button(frame, text='Borrar', command=self.borrar_tarea).grid(columnspan=2, row=10, sticky=W + E)

        # Boton Editar
        ttk.Button(frame, text='Editar').grid(columnspan=2, row=11, sticky=W + E)
        # Mensaje output
        self.message = Label(frame, text='', fg='red')
        self.message.grid(row=6, columnspan=2, sticky=W + E)

        # Se crea la tabla
        self.tree = ttk.Treeview(height=10, columns=('#1', '#2', '#3', '#4'))
        self.tree.grid(column=1, row=10, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Materia', anchor=CENTER)
        self.tree.heading('#2', text='Maestro', anchor=CENTER)
        self.tree.heading('#3', text='Descripción', anchor=CENTER)
        self.tree.heading('#4', text='Fecha', anchor=CENTER)

    # método que hace la conexión a la base de datos
    # cada vez que se quiera hacer una acción con la misma
    def run_query(self, query, parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parametros)
            conn.commit()
        return resultado

    # Muestra las tareas de la base de datos
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
            self.message['text'] = 'La tarea ha sido añadido de manera exitosa'
            # Limpia los entry
            self.nombre.delete(0, END)
            self.materia.delete(0, END)
            self.maestro.delete(0, END)
            self.descripcion.delete(0, END)
            self.fecha.delete(0, END)
        else:
            self.message['text'] = 'Por favor no dejes ningún campo en blanco'

    # Borrar una tarea seleccionada
    def borrar_tarea(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            self.message['text'] = 'Por favor selecciona una tarea!'
            return
        self.message['text'] = ''
        nombre = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM tareas WHERE nombre = ?'
        self.run_query(query, (nombre, ))
        self.message['text'] = 'La tarea ha sido borrada de manera exitosa!'
        self.get_tareas()


if __name__ == '__main__':
    window = Tk()
    application = Tarea(window)
    window.mainloop()
