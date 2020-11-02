import random
from tkinter import *
from winsound import PlaySound


def G_M():
    # ------------------------------------------------PROGRAMME PRINCIPAL---------------------------------------------------

    # Création et paramétrage de l'interface Tkinter
    fenetre = Tk()
    fenetre.title("Grapho_Mémoire")
    fenetre.resizable(width=False, height=False)

    # Création et paramétrage de l'interface Graphique Canvas
    Dessin = Canvas(fenetre, width=680, height=645, bg="white")
    Dessin.pack()

    # ---------------------------------------------------LES FONCTIONS------------------------------------------------------

    # ------FONCTIONS DE LA PARTIE------


    def Initialiser_jeu ():

        # initialisation des données du jeu
        global delai
        global nb_cartes_trouvees, liste_id_cartes, cartes_melangees, Nombre_Coups

        # initialisation du délai d'affichage des cartes (en ms)
        delai = random.choice([500, 600, 700, 800, 900, 1000, 1200])

        # initialisation des cartes trouvees et le nombre de coups
        nb_cartes_trouvees = 0
        Nombre_Coups = 0

        # Création d'une liste d'identifiants de cartes sur le canevas
        liste_id_cartes = Initialiser_canevas()

        # Création d'une liste aléatoire de 20 nombre entre 1 et 10 apparaissant deux fois
        cartes_melangees = Melanger_cartes()

        # Gestion des clics souris
        Clics_souris()


    def Initialiser_canevas ():
        # Remplissage du canevas avec les dos de cartes

        # Efface le canevas
        Dessin.delete(ALL)

        # initialisation de la liste des identifiants de cartes
        liste_ids = []

        # On parcourt les lignes
        for ligne in range(nb_lignes):

            # on parcourt les colonnes
            for colonne in range(nb_colonnes):

                # Positionnement des dos de cartes
                liste_ids.append(
                    Dessin.create_image(
                        110*colonne, 130*ligne,
                        anchor=NW, image=dos_carte, tags="cartes",
                    )
                )
        return liste_ids


    def Partie_Terminer ():
        # la partie est terminée

        # on efface le canevas
        Dessin.delete(ALL)

        # point central du canevas
        x, y = Dessin.winfo_reqwidth()//2, Dessin.winfo_reqheight()//2

        # Récupération du nombre de coups
        global Nombre_Coups, Meilleur_Score

        # Affiche d'un message de Fin
        Dessin.create_text(x, y-230, text="Vous avez trouvé", font="sans 60 bold", fill="green")
        Dessin.create_text(x-160, y-150, text="Tous les", font="sans 50 bold", fill="green")
        Dessin.create_text(x+160, y-150, text="Canards ! ", font="sans 50 bold", fill="dark orange")
        Dessin.create_text(x, y-30, text="En {} coups".format(Nombre_Coups), font="sans 32 bold", fill="dark blue")

        # Bouton rejouer
        Dessin.create_window(x, y+40, window=Button(Dessin, text="Rejouer", command=Initialiser_jeu))

        # Gestion du meilleurs score
        if Nombre_Coups < Meilleur_Score:
            Meilleur_Score = Nombre_Coups

        if Meilleur_Score == 0:
            Meilleur_Score = Nombre_Coups

        Dessin.create_text(x, y+180, text="Meilleur Score = {} coups".format(Meilleur_Score), font="sans 36 bold", fill="gold")

    # ------FONCTIONS DES CARTES------

    def Charger_images ():
        # Mise en mémoire des images des cartes

        # l'image0 est le dos des cartes
        nb_images = 1 + nb_total_cartes // 2
        images = []

        # on importe les images en mémoire
        for i in range(nb_images):

            # on ajoute une nouvelle image à la liste
            images.append(PhotoImage(file="Images_grapho_memoire/image{}.gif".format(i)))


        return images


    def Melanger_cartes ():
        # création d'une liste d'indices de cartes mélangés

        # liste des indices de cartes
        liste = list(range(1, nb_total_cartes//2 + 1)) * 2

        # on mélange les indices de cartes
        random.shuffle(liste)

        return liste


    def Valeur_carte (id_carte):
        # Renvoie la valeur de la carte correspondant à l'ID de canvasItem

        # initialisation index carte
        index = liste_id_cartes.index(id_carte)

        # valeur carte à cet emplacement
        return cartes_melangees[index]


    def Cacher_cartes ():
        # on retourne toutes les cartes du canevas
        Dessin.itemconfigure("cartes", image=dos_carte)

        # Données de clics souris
        Clics_souris()


    def Afficher_carte (id_carte):
        # Affiche la carte correspondant à l'ID de canvasItem

        # affichage de la carte
        Dessin.itemconfigure(id_carte, image=images[Valeur_carte(id_carte)])


    def Paire (id1, id2):
        # Vérifie si les deux cartes forme une paire
        return bool(Valeur_carte(id1) == Valeur_carte(id2))


    def Supprimer_cartes ():
        # suppression des paires trouvées

        global nb_cartes_trouvees

        # suppression cartes 1 et 2
        Dessin.delete(id_carte1)
        Dessin.delete(id_carte2)
        PlaySound("images_grapho_memoire/Ducksound", 1)

        # mise à jour du nombres de cartes trouvées
        nb_cartes_trouvees += 2

        # Si le nombre de carte trouvé est égal aux nombres de carte alors:
        if nb_cartes_trouvees >= nb_total_cartes:

            # Fin de la partie
            Partie_Terminer()

        # Sinon on continue la partie
        else:

            # données de clics souris
            Clics_souris()


    # ------FONCTIONS DES CLICS SOURIS------

    def Clics_souris ():
        # Remise à zéro des données de clics souris

        global id_carte1, id_carte2
        id_carte1 = id_carte2 = 0


    def Clics_souris_Event (event):
        # Gestionnaire événements des clics souris et du nombre de coup qui est lier

        global id_carte1, id_carte2, Nombre_Coups

        # initialisation des coordonnées du clic de la souris
        x, y = event.x, event.y

        # recherche de carte
        collisions = Dessin.find_overlapping(x, y, x, y)

        # Si le joueur clique sur une carte alors :
        if collisions and collisions[0] in liste_id_cartes:

            # initialise ID carte
            id_carte = collisions[0]

            # Première carte à retourner
            if id_carte1 == 0:

                # initialisation IDs cartes
                id_carte1 = id_carte
                id_carte2 = 0
                Afficher_carte(id_carte1)

            # Deuxième carte à retourner
            elif id_carte2 == 0 and id_carte != id_carte1:

                # initialisation ID carte
                id_carte2 = id_carte
                Afficher_carte(id_carte2)

                # Si une paire est trouvée alors :
                if Paire(id_carte1, id_carte2):

                    # suppression des cartes conserné par la paire au bout d'un délai
                    fenetre.after(delai, Supprimer_cartes)

                    # mise à jour du nombre de coups
                    Nombre_Coups += 2

                # Sinon pas de Paire trouvée alors :
                else:

                    # Re-cacher toutes les cartes au bout d'un délai
                    fenetre.after(delai, Cacher_cartes)

                    # Mise à jour du nombre de coups
                    Nombre_Coups += 2


    # ---------------------------------------------------LES VARIABLES------------------------------------------------------

    nb_lignes, nb_colonnes = 5, 6
    nb_total_cartes = nb_lignes * nb_colonnes

    global Meilleur_Score
    Meilleur_Score = 0

    # ------------------------------------------------PROGRAMME PRINCIPAL---------------------------------------------------

    # la liste images contient les 11 images (dos + 10 images)
    images = Charger_images()

    # initialisation des dos de cartes
    dos_carte = images[0]

    # initialisation des données du jeu
    Initialiser_jeu()

    Bouton_retour = Button(fenetre, text="Retour au menu principale", command=fenetre.destroy)
    Bouton_retour.pack()

    # gestionnaire des clics souris
    Dessin.bind('<Button-1>', Clics_souris_Event)

    # boucle principale
    fenetre.mainloop()