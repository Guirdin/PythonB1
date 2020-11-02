from tkinter import *
import tkinter

app = Tk()
app.geometry("500x500")
app.title("Exemple Tkinter")

def FonctionTaille():
    print("Ma fonction")


menu_principale = tkinter.Menu(app)

sou_menu = tkinter.Menu(menu_principale, tearoff=0)

menu_principale.add_cascade(label="Taille", menu=sou_menu)
sou_menu.add_command(label="taille1", command=FonctionTaille)


app.config(menu=menu_principale)
app.mainloop()