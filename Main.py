import tkinter as tk
import tkinter
from tkinter import *
import os
from TrianglesDivers import T_D
from GraphoMemoire import G_M
from EllipsesColorees import E_C
from SuperMind import S_M
from Divination import *
from VolumesDivers import *

def Main():

    Police_Titre = ("Helvetica", 18)

    def Triangles_Divers():
        T_D()

    def Grapho_Mémoire():
        app.destroy()
        G_M()
        Main()

    def Ellipses_Colorees():
        E_C()

    def Super_Mind():
        S_M()

    def Divination():
        os.system("Divination.py")

    def Volumes_Divers():
        os.system("VolumesDivers.py")


    class Application(tk.Tk):

        def __init__(self):
            tk.Tk.__init__(self)

            app = tk.Frame(self)
            app.pack(side="top", fill="both", expand=True)
            app.grid_rowconfigure(0, weight=1)
            app.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (Menu_Principal, Menu_Math, Menu_Jeux, Menu_Graphique):
                page_name = F.__name__
                frame = F(parent=app, controller=self)
                self.frames[page_name] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("Menu_Principal")

        def show_frame(self, page_name):

            frame = self.frames[page_name]
            frame.tkraise()


    class Menu_Principal(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            label = tk.Label(self, text="Veuillez choisir un Menu", font=Police_Titre)
            label.pack(side="top", fill="x", pady=10)

            bouton_Jeux = tk.Button(self, text="Jeux",
                                    command=lambda: controller.show_frame("Menu_Jeux"))
            bouton_Math = tk.Button(self, text="Math",
                                    command=lambda: controller.show_frame("Menu_Math"))
            bouton_Graphique = tk.Button(self, text="Graphique",
                                         command=lambda: controller.show_frame("Menu_Graphique"))
            bouton_Jeux.pack()
            bouton_Math.pack()
            bouton_Graphique.pack()


    class Menu_Math(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            label = tk.Label(self, text="Veuillez choisir un Programme", font=Police_Titre)
            label.pack(side="top", fill="x", pady=10)

            bouton_Volumes_Divers = tk.Button(self, text="Volumes Divers",
                               command=Volumes_Divers)
            bouton_Menu_Principale = tk.Button(self, text="Retour au Menu Principale",
                                               command=lambda: controller.show_frame("Menu_Principal"))
            bouton_Volumes_Divers.pack()
            bouton_Menu_Principale.pack()


    class Menu_Jeux(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            label = tk.Label(self, text="Veuillez Choisir un Jeu", font=Police_Titre)
            label.pack(side="top", fill="x", pady=10)

            bouton_Divination = tk.Button(self, text="Divination",
                                          command=Divination)
            bouton_Super_Mind = tk.Button(self, text="Super Mind",
                                          command=Super_Mind)
            bouton_Grapho_Mémoire = tk.Button(self, text="Grapho Mémoire",
                                              command=Grapho_Mémoire)
            bouton_Menu_Principale = tk.Button(self, text="Retour au Menu Principale",
                                               command=lambda: controller.show_frame("Menu_Principal"))

            bouton_Divination.pack()
            bouton_Super_Mind.pack()
            bouton_Grapho_Mémoire.pack()
            bouton_Menu_Principale.pack()


    class Menu_Graphique(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            label = tk.Label(self, text="Veuillez choisir un programme", font=Police_Titre)
            label.pack(side="top", fill="x", pady=10)

            bouton_Triangle_Divers = tk.Button(self, text="Triangle Divers",
                               command=Triangles_Divers)
            bouton_Ellipses_Colorees = tk.Button(self, text="Ellispses Colorées",
                               command=Ellipses_Colorees)
            bouton_Menu_Principale = tk.Button(self, text="Retour au Menu Principale",
                                               command=lambda: controller.show_frame("Menu_Principal"))
            bouton_Triangle_Divers.pack()
            bouton_Ellipses_Colorees.pack()
            bouton_Menu_Principale.pack()

    if __name__ == "__main__":
        app = Application()
        app.mainloop()
Main()