import tkinter as tk
import tkinter
from tkinter import *
import random
import os


global point
point = 0

def divination():
    Police_Titre = ("Helvetica", 18)

    class Application(tk.Tk):

        def __init__(self):
            tk.Tk.__init__(self)

            app = tk.Frame(self)
            app.pack(side="top", fill="both", expand=True)
            app.grid_rowconfigure(0, weight=1)
            app.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (Jeu_divination, Fin):
                page_name = F.__name__
                frame = F(parent=app, controller=self)
                self.frames[page_name] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("Jeu_divination")


        def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()



    class Jeu_divination(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller


            label = tk.Label(self, text="Bienvenue dans le jeu de divination", font=Police_Titre)
            label.pack(side="top", fill="x", pady=10)

            #Le canvas contenant la carte coté face
            can = Canvas(self, width=300, height=300)
            can.pack(side='left', padx=10, pady=40)

            #La valeur de la carte cote face est detenu par le carteFaceRandom
            self.carteFaceRandom = random.randint(1, 13)
            self.img = PhotoImage()

            #Afin d'afficher la carte selon le numéro tiré dans le random
            if self.carteFaceRandom == 1:
                self.img = PhotoImage(file='images/cartes1.gif')
            if self.carteFaceRandom == 2:
                self.img = PhotoImage(file='images/cartes2.gif')
            if self.carteFaceRandom == 3:
                self.img = PhotoImage(file='images/cartes3.gif')
            if self.carteFaceRandom == 4:
                self.img = PhotoImage(file='images/cartes4.gif')
            if self.carteFaceRandom == 5:
                self.img = PhotoImage(file='images/cartes5.gif')
            if self.carteFaceRandom == 6:
                self.img = PhotoImage(file='images/cartes6.gif')
            if self.carteFaceRandom == 7:
                self.img = PhotoImage(file='images/cartes7.gif')
            if self.carteFaceRandom == 8:
                self.img = PhotoImage(file='images/cartes8.gif')
            if self.carteFaceRandom == 9:
                self.img = PhotoImage(file='images/cartes9.gif')
            if self.carteFaceRandom == 10:
                self.img = PhotoImage(file='images/cartes10.gif')
            if self.carteFaceRandom == 11:
                self.img = PhotoImage(file='images/cartes11.gif')
            if self.carteFaceRandom == 12:
                self.img = PhotoImage(file='images/cartes12.gif')
            if self.carteFaceRandom == 13:
                self.img = PhotoImage(file='images/cartes13.gif')

            #Afin de placer l'image dans le canvas
            can.create_image(120, 180, image=self.img)

            #Le canvas contenant l'image retournée
            canny = Canvas (self, width=300, height=300)
            canny.pack(side='right', padx=5, pady=1)
            self.img2 = PhotoImage(file="images/interrogation.gif")

            #La valeur de la carte a deviner est detenu par le carteRetourneeRandom
            self.carteRetourneeRandom = random.randint(1, 13)
            canny.create_image(120, 180, image=self.img2)

            #Les boutons pour savoir si la carte retournée est plus grande ou plus petite
            canno = Canvas(self, width=50, height=50)
            canno.pack(side=BOTTOM)
            bouton_grand = tk.Button(canno, text="Plus grand", command=self.plus_grand)
            bouton_grand.pack(side=LEFT)
            bouton_petit = tk.Button(canno, text="Plus petit", command=self.plus_petit)
            bouton_petit.pack(side=RIGHT)
            Quitter = Button(canno, text='Quitter', command=self.quit)
            Quitter.pack(padx=20)


        def plus_grand(self):
            if self.carteRetourneeRandom > self.carteFaceRandom:
                message = Label(text='C\'était bien plus grand.')
                message.pack()
                self.gagner()
            if self.carteRetourneeRandom < self.carteFaceRandom :
                msg = Label(text='C\'était plus petit.')
                msg.pack()
                self.perdu()


        def plus_petit(self):
            if self.carteRetourneeRandom < self.carteFaceRandom:
                messpetit = Label(text='C\'était bien plus petit.')
                messpetit.pack()
                self.gagner()
            if self.carteRetourneeRandom > self.carteFaceRandom:
                messpet = Label(text='C\'était plus grand.')
                messpet.pack()
                self.perdu()


        def continuer(self):
            app.destroy()
            divination()


        def gagner(self):
            messageGagner = Label(text='Vous avez bien trouvé, vous pouvez continuer à jouer')
            messageGagner.pack()
            global point
            point += 10
            messagePoint = Label(text='Vos points = {}'.format(point))
            messagePoint.pack()
            continuer = Button(self, text='Continuer', command=self.continuer)
            continuer.pack()


        def perdu(self):
            messagePerdu = Label(text='Vous avez perdu. Vous pouvez recommencer à jouer.')
            messagePerdu.pack()
            global point
            point = 0
            recommencer = Button(self, text='Recommencer', command=self.continuer)
            recommencer.pack()


    class Fin(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller



    if __name__ == "__main__":
        app = Application()
        app.mainloop()
divination()
