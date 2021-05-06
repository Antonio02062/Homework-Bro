from assets import *
from tkinter import *
from tkinter import ttk

def openAddHwk():
    newHkwWin = Tk()

    newHkwWin.title("Tarea Nueva")
    #newHkwWin.geometry("320x200")
    newHkwWin.configure(bg=mainColor)

    labelStyle = ttk.Style()
    labelStyle.configure(
        "labelStyle.TLabel",
        bg = mainColor,
        fg = secondaryColor4,
        padding = 0,
        borderwidth = 0
    )
    nameLabel = ttk.Label(newHkwWin, text = "Titulo:", style = "labelStyle.TLabel", font = mainFont)
    nameLabel.grid(column = 0, row = 0)

    nameEntry = ttk.Entry(newHkwWin)
    nameEntry.grid(column = 1, row = 0)


    newHkwWin.mainloop()


