from tkinter import *

def clignotement_rect():
    global rect_status
    global rect
    # Si le rectangle est affiché
    if rect_status == 'place':
        # On le cache et on change son statut
        canvas.delete(rect)
        rect_status = 'not_place'
    else:
        # On l'affiche et on change son status
        rect = canvas.create_rectangle(base_x, base_y, base_x+large, base_y+hauteur, fill='red')
        canvas.pack()
        rect_status = 'place'

        # Et on boucle tout les 143ms soit 7Hz
    fenetre.after(143, clignotement_rect)

def clignotement_tri():
    global tri_status
    global tri
    # Si le triangle est affiché
    if tri_status == 'place':
        # On le cache et on change son statut
        canvas.delete(tri)
        tri_status = 'not_place'
    else:
        # On l'affiche et on change son status
        tri = canvas.create_polygon(x0, y0, x1, y1, x2, y2,fill='green')
        canvas.pack()
        tri_status = 'place'

        # Et on boucle tout les 71ms soit 14Hz
    fenetre.after(71, clignotement_tri)

def clignotement_oval():
    global oval_status
    global oval
    # Si le triangle est affiché
    if oval_status == 'place':
        # On le cache et on change son statut
        canvas.delete(oval)
        oval_status = 'not_place'
    else:
        # On l'affiche et on change son status
        oval = canvas.create_oval(x2+espacement_x,base_y,x2+espacement_x+large,base_y+hauteur,fill='yellow')
        canvas.pack()
        oval_status = 'place'

        # Et on boucle tout les 47ms soit 21Hz
    fenetre.after(47, clignotement_oval)

rect_status='place'
tri_status='place'
oval_status='place'

fenetre = Tk()
xmax=1250
ymax=500
fenetre.geometry("1250x500")
canvas = Canvas(fenetre, width=1250, heigh=500, background='grey')
# Coordonée clé
large = 175
hauteur = 175
base_x = 150
base_y = 250-large/2
espacement_x = 200
# Création forme
rect = canvas.create_rectangle(base_x, base_y, base_x+large,base_y+hauteur, fill='red')
x0 = base_x+large+espacement_x; y0 = base_y+hauteur
x1 = x0+large/2; y1 = base_y
x2 = x0+large; y2 = y0
tri = canvas.create_polygon(x0, y0, x1, y1, x2, y2,fill='green')
oval = canvas.create_oval(x2+espacement_x,base_y,x2+espacement_x+large,base_y+hauteur,fill='yellow')
canvas.pack()
# Methode
clignotement_rect()
clignotement_tri()
clignotement_oval()

fenetre.mainloop()

