from random import *
from tkinter import *

root = Tk()
root.title("Super Mind")
root.geometry("550x300")

Police_Titre = ("Helvetica", 18)

global listeNombres, uncover, essais, win
listeNombres = []
uncover = []
essais = 0
win = False

def Initilisation_niveau():
    D = int(Difficulté.get())
    global n, x, Proposition, uncover, i
    n = D+2
    for i in range(0,n):
        nombreRandom = randint(1,9)
        listeNombres.append(nombreRandom)

    for x in range(0, n):
        uncover.append('*')
    print("La liste est :", uncover)

    Choix_Difficulté.destroy()
    Difficulté.destroy()
    Valider_Difficulté.destroy()
    Affiche_liste = Label(root, text="La liste est :" + uncover[x])
    Affiche_liste.pack()

    Proposition = Entry(root)
    Proposition.pack()

    Valider_Proposition = Button(root, text="Valider", command=Jeu)
    Valider_Proposition.pack()

def Jeu():
    global win, Proposition, essais, listeNombres, i
    while win == False:
        P = len(Proposition.get())
        if P == n:
            winCount = 0
            essais +=1
            listNbProp = []
            listExists = []
            for i in range(0,n):
                listNbProp.append(P[i])
            for i in range(0,n):
                if listNbProp[i] == listeNombres[i]:
                    uncover[i] = listNbProp[i]
                    winCount = winCount+1
                elif listNbProp[i] in listeNombres:
                    listExists.append(listNbProp[i])
            print("Tu as découvert ",uncover)
            print(listExists," existent mais ne sont pas bien placés")

            if winCount == n:
                win = True

    print('\nBravo ! Tu as gagné en ', essais, ' essai(s).')

Choix_Difficulté = Label(root, text="Veuillez choisir une difficulté", font=Police_Titre)
Choix_Difficulté.pack()

Difficulté = Entry(root)
Difficulté.pack()

Valider_Difficulté = Button(root, text="Valider", command=Initilisation_niveau)
Valider_Difficulté.pack()



root.mainloop()