import tkinter
from tkinter import *

def T_D():

    # ------------------------------------------------PROGRAMME PRINCIPAL---------------------------------------------------

    # Création et paramétrage de l'espace déssin et de l'interface Tkinter
    TD = Tk()
    Dessin = Canvas(TD, width=625, height=600, bg='white')
    Dessin.pack(side=TOP, padx=5, pady=5)
    TD.geometry("625x600")
    TD.title("Triangles Divers")

    # ---------------------------------------------------LES FONCTIONS------------------------------------------------------

    def delete(MonTag):
        Dessin.delete(Dessin.find_withtag(MonTag))



    # ------FONCTIONS TAILLES-----

    def Taille1():
        if Dessin.find_withtag!=('Taille1'):
            delete('all')
        #                 ( ligne de Gauche  ;  ligne du centre  ;  Ligne de Droite  )
        Dessin.create_line(270, 300, 300, 270, 270, 300, 330, 300, 300, 270, 330, 300, fill=couleur, width=Trait, tags="Taille1")
        #                 ( x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 )

    def Taille2():
        if Dessin.find_withtag != ('Taille2'):
            delete('all')
        #                 ( ligne de Gauche  ;  ligne du centre  ;  Ligne de Droite  )
        Dessin.create_line(240, 300, 300, 240, 240, 300, 360, 300, 300, 240, 360, 300, fill=couleur, width=Trait, tags="Taille2")
        #                 ( x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 )

    def Taille3():
        if Dessin.find_withtag!=('Taille3'):
            delete('all')
        #                 ( ligne de Gauche  ;  ligne du centre  ;  Ligne de Droite  )
        Dessin.create_line(210, 300, 300, 210, 210, 300, 390, 300, 300, 210, 390, 300, fill=couleur, width=Trait, tags="Taille3")
        #                 ( x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 )

    def Taille4():
        if Dessin.find_withtag!=('Taille4'):
            delete('all')
        #                 ( ligne de Gauche  ;  ligne du centre  ;  Ligne de Droite  )
        Dessin.create_line(180, 300, 300, 180, 180, 300, 420, 300, 300, 180, 420, 300, fill=couleur, width=Trait, tags="Taille4")
        #                 ( x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 )

    def Taille5():
        if Dessin.find_withtag!=('Taille5'):
            delete('all')
        #                 ( ligne de Gauche  ;  ligne du centre  ;  Ligne de Droite  )
        Dessin.create_line(150, 300, 300, 150,
                           150, 300, 450, 300,
                           300, 150, 450, 300,
                           
                           fill=couleur, width=Trait, tags="Taille5")
        #                 ( x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 )

    def Taille6():
        if Dessin.find_withtag!=('Taille6'):
            delete('all')
        #                 ( ligne de Gauche  ;  ligne du centre  ;  Ligne de Droite  )
        Dessin.create_line(120, 300, 300, 120, 120, 300, 480, 300, 300, 120, 480, 300, fill=couleur, width=Trait, tags="Taille6")
        #                 ( x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 )

    def Taille7():
        if Dessin.find_withtag!=('Taille7'):
            delete('all')
        #                 ( ligne de Gauche  ;  ligne du centre  ;  Ligne de Droite  )
        Dessin.create_line(90, 300, 300, 90, 90, 300, 510, 300, 300, 90, 510, 300, fill=couleur, width=Trait, tags="Taille7")
        #                 ( x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 ;  x1,  y1,  x2, y2 )

    def Taille8():
        if Dessin.find_withtag!=('Taille8'):
            delete('all')
        #                 ( ligne de Gauche ;  ligne du centre ;  Ligne de Droite)
        Dessin.create_line(60, 300, 300, 60, 60, 300, 550, 300, 300, 60, 550, 300, fill=couleur, width=Trait, tags="Taille8")
        #                 (x1,  y1,  x2, y2; x1,  y1,  x2, y2 ;  x1, y1,  x2, y2 )

    def Taille9():
        global couleur, Trait
        if Dessin.find_withtag!=('Taille9'):
            delete('all')
        #                 ( ligne de Gauche ;  ligne du centre ;  Ligne de Droite)
        Dessin.create_line(30, 300, 300, 30, 30, 300, 590, 300, 300, 30, 590, 300, fill=couleur, width=Trait, tags="Taille9")
        #                 (x1,  y1,  x2, y2; x1,  y1,  x2, y2 ;  x1, y1,  x2, y2 )


    # ---------------------------------------------------Valeurs par défault------------------------------------------------------

    # Globalisation des variables couleur et trait
    global couleur, Trait

    # Couleur par défault
    couleur = 'Black'
    # Trait par défault
    Trait = '3'
    # Taille par défault:
    Taille5()



    # -----FONCTIONS COULEURS-------

    def Bleu():
        global couleur
        couleur = 'blue'

    def Vert():
        global couleur
        couleur = 'green'

    def Rouge():
        global couleur
        couleur = 'red'

    def Orange():
        global couleur
        couleur = 'orange'

    def Violet():
        global couleur
        couleur = 'purple'


    # -----FONCTIONS TRAITS-------

    def Fort():
        global Trait
        Trait = '6'

    def normal():
        global Trait
        Trait = '3'

    def Fin():
        global Trait
        Trait = '1'

    # ------------------------------------------------PROGRAMME PRINCIPAL---------------------------------------------------

    # Création des Menus
    Menu_Principal = tkinter.Menu(TD)
    Taille_menu = tkinter.Menu(Menu_Principal, tearoff=0)
    Couleur_menu = tkinter.Menu(Menu_Principal, tearoff=0)
    Trait_menu = tkinter.Menu(Menu_Principal, tearoff=0)

    # Paramétrage des Menus
    Menu_Principal.add_cascade(label="Forme du Trait", menu=Trait_menu)
    Menu_Principal.add_cascade(label="Couleur", menu=Couleur_menu)
    Menu_Principal.add_cascade(label="Taille", menu=Taille_menu)


    # Commande du Menu Trait
    Trait_menu.add_command(label="Trait Fort", command=Fort)
    Trait_menu.add_command(label="Trait Normal", command=normal)
    Trait_menu.add_command(label="Trait Fin", command=Fin)

    # Commande du Menu Couleur
    Couleur_menu.add_command(label="Bleu", command=Bleu)
    Couleur_menu.add_command(label="Vert", command=Vert)
    Couleur_menu.add_command(label="Rouge", command=Rouge)
    Couleur_menu.add_command(label="Orange", command=Orange)
    Couleur_menu.add_command(label="Violet", command=Violet)

    # Commande du Menu Taille
    Taille_menu.add_command(label="Taille 1", command=Taille1)
    Taille_menu.add_command(label="Taille 2", command=Taille2)
    Taille_menu.add_command(label="Taille 3", command=Taille3)
    Taille_menu.add_command(label="Taille 4", command=Taille4)
    Taille_menu.add_command(label="Taille 5", command=Taille5)
    Taille_menu.add_command(label="Taille 6", command=Taille6)
    Taille_menu.add_command(label="Taille 7", command=Taille7)
    Taille_menu.add_command(label="Taille 8", command=Taille8)
    Taille_menu.add_command(label="Taille 9", command=Taille9)


    # Boucle Principal
    TD.config(menu=Menu_Principal)
    TD.mainloop()