import tkinter.filedialog
from tkinter import *

from tkinter import ttk

app = Tk()

menu = Menu(app)
file_menu = Menu(menu)
option_menu = Menu(menu)

menu.add_cascade(label='File', menu=file_menu)
text_area = Text(app, font=("consolas", 11))
text_area.pack(fill=BOTH, expand=1)


def save():
    f = tkinter.filedialog.asksaveasfile(initialfile="Untitled.txt", defaultextension=".txt",
                                         filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if f is None:
        return
    text2save = str(text_area.get(1.0, END))
    f.write(text2save)
    f.close()
    print(f.name)


file_menu.add_command(label="Save", command=save)

app.config(menu=menu)

app.mainloop()
