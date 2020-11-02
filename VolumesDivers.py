import tkinter as tk
import tkinter
from tkinter import *
from math import *
import os


Police_Titre = ("Helvetica", 18)
Police_Sous_Titre = ("Helvetica", 11)
Police_Ecriture = ("Helvetica", 9)

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        app = tk.Frame(self)
        app.pack(side="top", fill="both", expand=True)
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu_Principal, Cube, Para_rectangle, Sphere, Cylindre, Pyramide):
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

        label = tk.Label(self, text="Veuillez choisir un menu", font=Police_Titre)
        label.pack(side="top", fill="x", pady=10)

        bouton_cube = tk.Button(self, text="Cube",
                                command=lambda: controller.show_frame("Cube"))
        bouton_cube.pack()
        bouton_para = tk.Button(self, text="Parallélépipède rectangle",
                                command=lambda: controller.show_frame("Para_rectangle"))
        bouton_para.pack()
        bouton_cylindre = tk.Button(self, text="Cylindre",
                                command=lambda: controller.show_frame("Cylindre"))
        bouton_cylindre.pack()
        bouton_sphere = tk.Button(self, text="Sphère",
                                command=lambda: controller.show_frame("Sphere"))
        bouton_sphere.pack()
        bouton_pyramide = tk.Button(self, text="Pyramide",
                                command=lambda: controller.show_frame("Pyramide"))
        bouton_pyramide.pack()

class Cube(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Vous avez choisi pour calculer le volume d'un cube. Sa formule est : V = cote^3 .\nEntrez les valeurs de votre cube.",
                         font=Police_Sous_Titre)
        label.pack(side="top", fill="x", pady=10)
        message = tk.Label(self, text='Veuillez saisir la valeur du côté de votre cube : ', font=Police_Ecriture)
        message.pack()

        Resultat = DoubleVar()
        def puissance_cube():
            Resultat.set("Le résultat est "+str(float(valeur.get()) * (valeur.get()) * (valeur.get())))


        valeur = DoubleVar()
        var = 2.0
        # Création d'un widget Spinbox pour la valeur a rentrer
        valeur.set(var)
        boite = Spinbox(self, from_=0, to=10, increment=0.1, textvariable=valeur, width=6)
        boite.pack(padx=30, pady=10)
        button = tk.Button(self, text='Valider', command=puissance_cube)
        button.pack()


        Label(self, textvariable=Resultat).pack(padx=30, pady=10)
        #Revenir au menu principal
        bouton_Menu_Principal = tk.Button(self, text="Retour au menu principale",
                           command=lambda: controller.show_frame("Menu_Principal"))
        bouton_Menu_Principal.pack()

class Para_rectangle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self,
                         text="Vous avez choisi pour calculer le volume d'un parallélépipède rectangle. Sa formule est : V = largeur * longueur * hauteur .\nEntrez les valeurs de votre parallélépipède rectangle.",
                         font=Police_Sous_Titre)
        label.pack(side="top", fill="x", pady=10)
        Resultat = DoubleVar()

        def calcul_volume():
            Resultat.set("Le résultat est " + str(float(valeur_largeur.get()) * (valeur_longueur.get()) * (valeur_hauteur.get())))

        valeur_largeur = DoubleVar()
        valeur_longueur = DoubleVar()
        valeur_hauteur = DoubleVar()
        var = 2.0

        # Création d'un widget Spinbox pour la valeur a rentrer
        valeur_largeur.set(var)
        valeur_longueur.set(var)
        valeur_hauteur.set(var)

        # boite + bouton largeur
        message = tk.Label(self, text='Largeur (en cm) : ', font=Police_Ecriture)
        message.pack()
        boite = Spinbox(self, from_=0, to=10, increment=0.1, textvariable=valeur_largeur, width=6)
        boite.pack(padx=30, pady=10)
        button = tk.Button(self, text='Valider', command=calcul_volume)
        button.pack(anchor=CENTER)

        # boite + bouton longueur
        message2 = tk.Label(self, text='Longueur (en cm) : ', font=Police_Ecriture)
        message2.pack()
        boite = Spinbox(self, from_=0, to=10, increment=0.1, textvariable=valeur_longueur, width=6)
        boite.pack(padx=30, pady=10)
        button = tk.Button(self, text='Valider', command=calcul_volume)
        button.pack(anchor=CENTER)

        # boite + bouton hauteur
        message3 = tk.Label(self, text='Hauteur (en cm) : ', font=Police_Ecriture)
        message3.pack()
        boite = Spinbox(self, from_=0, to=10, increment=0.1, textvariable=valeur_hauteur, width=6)
        boite.pack(padx=30, pady=10)
        button = tk.Button(self, text='Valider', command=calcul_volume)
        button.pack(anchor=CENTER)


        Label(self, textvariable=Resultat).pack(padx=30, pady=10)
        # Revenir au menu principal
        bouton_Menu_Principal = tk.Button(self, text="Retour au menu principale",
                                          command=lambda: controller.show_frame("Menu_Principal"))
        bouton_Menu_Principal.pack()

class Cylindre(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Vous avez choisi pour calculer le volume d'un cylindre. Sa formule est : V = Pi * rayon^2 * hauteur .\nEntrez les valeurs de votre cylindre.",
                         font=Police_Sous_Titre)
        label.pack(side="top", fill="x", pady=10)
        Resultat = DoubleVar()

        def calcul_volume():
            Resultat.set("Le résultat est " + str(float(pi * ((valeur_rayon.get()) * valeur_rayon.get()))* (valeur_hauteur.get())))

        valeur_hauteur = DoubleVar()
        valeur_rayon = DoubleVar()
        var = 2.0

        # Création d'un widget Spinbox pour la valeur a rentrer
        valeur_hauteur.set(var)
        valeur_rayon.set(var)

        # boite + bouton hauteur
        message = tk.Label(self, text='Hauteur (en cm) : ', font=Police_Ecriture)
        message.pack()
        boite = Spinbox(self, from_=0, to=10, increment=0.1, textvariable=valeur_hauteur, width=6)
        boite.pack(padx=30, pady=10)
        button = tk.Button(self, text='Valider', command=calcul_volume)
        button.pack(anchor=CENTER)

        # boite + bouton rayon
        message2 = tk.Label(self, text='Rayon (en cm) : ', font=Police_Ecriture)
        message2.pack()
        boite = Spinbox(self, from_=0, to=10, increment=0.1, textvariable=valeur_rayon, width=6)
        boite.pack(padx=30, pady=10)
        button = tk.Button(self, text='Valider', command=calcul_volume)
        button.pack(anchor=CENTER)


        Label(self, textvariable=Resultat).pack(padx=30, pady=10)
        # Revenir au menu principal
        bouton_Menu_Principal = tk.Button(self, text="Retour au menu principale",
                                          command=lambda: controller.show_frame("Menu_Principal"))
        bouton_Menu_Principal.pack()

class Sphere(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self,
                         text="Vous avez choisi pour calculer le volume d'une sphère. Sa formule est : V = (4 * Pi * rayon^3)/3 .\nEntrez les valeurs de votre sphère.",
                         font=Police_Sous_Titre)
        label.pack(side="top", fill="x", pady=10)
        Resultat = DoubleVar()

        def calcul_volume():
            Resultat.set("Le résultat est " + str(float((4 * pi * (valeur_rayon.get() * valeur_rayon.get() * valeur_rayon.get())) / 3) ))

        valeur_rayon = DoubleVar()
        var = 2.0

        # Création d'un widget Spinbox pour la valeur a rentrer
        valeur_rayon.set(var)

        # boite + bouton rayon
        message2 = tk.Label(self, text='Rayon (en cm) : ', font=Police_Ecriture)
        message2.pack()
        boite = Spinbox(self, from_=0, to=10, increment=0.1, textvariable=valeur_rayon, width=6)
        boite.pack(padx=30, pady=10)
        button = tk.Button(self, text='Valider', command=calcul_volume)
        button.pack(anchor=CENTER)

        Label(self, textvariable=Resultat).pack(padx=30, pady=10)
        # Revenir au menu principal
        bouton_Menu_Principal = tk.Button(self, text="Retour au menu principale",
                                          command=lambda: controller.show_frame("Menu_Principal"))
        bouton_Menu_Principal.pack()

class Pyramide(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self,
                         text="Vous avez choisi pour calculer le volume d'une pyramide. Sa formule est : V = (cote^2 * hauteur)/3 .\nEntrez les valeurs de votre pyramide.",
                         font=Police_Sous_Titre)
        label.pack(side="top", fill="x", pady=10)
        Resultat = DoubleVar()

        def calcul_volume():
            Resultat.set("Le résultat est " + str(float(((valeur_cote.get() * valeur_cote.get()) * valeur_hauteur.get()) / 3)))

        valeur_cote = DoubleVar()
        valeur_hauteur = DoubleVar()
        var = 2.0

        # Création d'un widget Spinbox pour la valeur a rentrer
        valeur_cote.set(var)
        valeur_hauteur.set(var)

        # boite + bouton côté
        message2 = tk.Label(self, text='Côté (en cm) : ', font=Police_Ecriture)
        message2.pack()
        boite = Spinbox(self, from_=0, to=10, increment=0.1, textvariable=valeur_cote, width=6)
        boite.pack(padx=30, pady=10)
        button = tk.Button(self, text='Valider', command=calcul_volume)
        button.pack(anchor=CENTER)

        # boite + bouton hauteur
        message = tk.Label(self, text='Hauteur (en cm) : ', font=Police_Ecriture)
        message.pack()
        boite = Spinbox(self, from_=0, to=10, increment=0.1, textvariable=valeur_hauteur, width=6)
        boite.pack(padx=30, pady=10)
        button = tk.Button(self, text='Valider', command=calcul_volume)
        button.pack(anchor=CENTER)


        Label(self, textvariable=Resultat).pack(padx=30, pady=10)
        # Revenir au menu principal
        bouton_Menu_Principal = tk.Button(self, text="Retour au menu principale",
                                          command=lambda: controller.show_frame("Menu_Principal"))
        bouton_Menu_Principal.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()