from tkinter import *

def E_C():

    global x0, x1, y0, y1, couleurInt, couleurExt
    winEllipses = Tk()
    canEllipses = Canvas(winEllipses, width=500, height=500)
    canEllipses.pack()
    x0=200
    y0=200
    x1=300
    y1=300
    couleurInt='white'
    couleurExt='black'


    ###FONCTIONS###

    def Taille1():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        x0 = 240
        x1 = 260
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Taille2():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        x0 = 220
        x1 = 280
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Taille3():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        x0 = 190
        x1 = 310
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Taille4():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        x0 = 175
        x1 = 325
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Taille5():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        x0 = 150
        x1 = 350
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Taille6():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        x0 = 125
        x1 = 375
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Taille7():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        x0 = 100
        x1 = 400
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Taille8():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        x0 = 75
        x1 = 425
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Taille9():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        x0 = 475
        x1 = 25
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)


    def CouleurBleuI():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurInt='blue'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurTurquoiseI():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurInt='turquoise1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurVertI():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurInt='green'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurOliveI():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurInt='OliveDrab1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurRoseI():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurInt='DeepPink1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurOrangeI():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurInt='DarkOrange1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurCyanI():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurInt='cyan'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurBleuCielI():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurInt='SkyBlue1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurJauneI():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurInt='yellow'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)


    def CouleurBleuE():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurExt='blue'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurTurquoiseE():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurExt='turquoise1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurVertE():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurExt='green'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurOliveE():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurExt='OliveDrab1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurRoseE():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurExt='DeepPink1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurOrangeE():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurExt='DarkOrange1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurCyanE():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurExt='cyan'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurBleuCielE():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurExt='SkyBlue1'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def CouleurJauneE():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        couleurExt='yellow'
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Applatissement1():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        y0 = 50
        y1 = 450
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Applatissement2():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        y0 = 100
        y1 = 400
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Applatissement3():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        y0 = 200
        y1 = 300
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Applatissement4():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        y0 = 175
        y1 = 325
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    def Applatissement5():
        global x0, x1, y0, y1, couleurInt, couleurExt
        for i in canEllipses.find_all():
            canEllipses.delete(i)
        y0 = 225
        y1 = 275
        canEllipses.create_oval(x0, y0, x1, y1, width=2, fill=couleurInt, outline=couleurExt)

    ###

    mainmenu = Menu(winEllipses)


    menuTailles = Menu(mainmenu)
    menuCouleurs = Menu(mainmenu)
    Hauteur=Menu(menuTailles)
    Longueur=Menu(menuTailles)

    Longueur.add_command(label="Taille 1", command=Taille1)
    Longueur.add_command(label="Taille 2", command=Taille2)
    Longueur.add_command(label="Taille 3", command=Taille3)
    Longueur.add_command(label="Taille 4", command=Taille4)
    Longueur.add_command(label="Taille 5", command=Taille5)
    Longueur.add_command(label="Taille 6", command=Taille6)
    Longueur.add_command(label="Taille 7", command=Taille7)
    Longueur.add_command(label="Taille 8", command=Taille8)
    Longueur.add_command(label="Taille 9", command=Taille9)

    Hauteur.add_command(label="Taille 1", command=Applatissement1)
    Hauteur.add_command(label="Taille 2", command=Applatissement2)
    Hauteur.add_command(label="Taille 3", command=Applatissement3)
    Hauteur.add_command(label="Taille 4", command=Applatissement4)
    Hauteur.add_command(label="Taille 5", command=Applatissement5)

    mainmenu.add_cascade(label = "Tailles", menu=menuTailles)
    mainmenu.add_cascade(label = "Couleurs", menu=menuCouleurs)
    menuTailles.add_cascade(label = "Longueur", menu=Longueur)
    menuTailles.add_cascade(label = "Hauteur", menu=Hauteur)

    CouleurInt = Menu(menuCouleurs)
    CouleurExt = Menu(menuCouleurs)
    menuCouleurs.add_cascade(label = "Intérieur", menu=CouleurInt)
    menuCouleurs.add_cascade(label = "Extérieur", menu=CouleurExt)
    CouleurInt.add_command(label="Bleu", command=CouleurBleuI)
    CouleurInt.add_command(label="Turquoise", command=CouleurTurquoiseI)
    CouleurInt.add_command(label="Vert", command=CouleurVertI)
    CouleurInt.add_command(label="Olive", command=CouleurOliveI)
    CouleurInt.add_command(label="Rose", command=CouleurRoseI)
    CouleurInt.add_command(label="Orange", command=CouleurOrangeI)
    CouleurInt.add_command(label="Cyan", command=CouleurCyanI)
    CouleurInt.add_command(label="Bleu Ciel", command=CouleurBleuCielI)
    CouleurInt.add_command(label="Jaune", command=CouleurJauneI)

    CouleurExt.add_command(label="Bleu", command=CouleurBleuE)
    CouleurExt.add_command(label="Turquoise", command=CouleurTurquoiseE)
    CouleurExt.add_command(label="Vert", command=CouleurVertE)
    CouleurExt.add_command(label="Olive", command=CouleurOliveE)
    CouleurExt.add_command(label="Rose", command=CouleurRoseE)
    CouleurExt.add_command(label="Orange", command=CouleurOrangeE)
    CouleurExt.add_command(label="Cyan", command=CouleurCyanE)
    CouleurExt.add_command(label="Bleu Ciel", command=CouleurBleuCielE)
    CouleurExt.add_command(label="Jaune", command=CouleurJauneE)

    winEllipses.config(menu = mainmenu)


    winEllipses.mainloop()
