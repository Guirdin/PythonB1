from random import *
from tkinter import *

def S_M():

    listeNombres = []
    uncover = []
    essais = 0
    win = False

    dif=int(input("Veuillez entrer votre difficulté\n"))
    n = dif+2
    for i in range(0,n):
        nombreRandom = randint(1,9)
        listeNombres.append(nombreRandom)

    for i in range(0,n):
        uncover.append('*')

    print("La liste est :", uncover)


    while win == False:
        proposition = input("\nQuelle est votre proposition ?\n")
        if len(proposition) == n:
            winCount = 0
            essais = essais+1
            listNbProp = []
            listExists = []
            for i in range(0,n):
                listNbProp.append(int(proposition[i]))
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