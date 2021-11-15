import turtle

fred= turtle.Turtle()

def carre(tortue,L):
    for i in range(4):
        tortue.forward(L)
        tortue.right(90)
    return None


        
def choix_couleur(nombre):
    if nombre % 2 == 0:
       return 'white'
    else: return 'black'
    
    
assert(choix_couleur(3) == 'black')

def decalage(indice):
    if indice % 6 == 0 or 1 or 2:
        return 20
    else: return -20
    
def carre_colore(tortue, L, nombre):
    couleur= choix_couleur(nombre)
    tortue.begin_fill()
    tortue.fillcolor(couleur)
    carre(tortue,L)
    tortue.end_fill()
    return None
    


def ligne_de_carre(L, n):
    for i in range(6):
        carre_colore(fred, 100, 5)