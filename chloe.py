import turtle
fred= turtle.Turtle()

def carre (fred,L):
    for i in range (4):
        fred.forward(L)
        fred.right(90)
    
solution= carre(fred,100)
fred.fd(100)
carre(fred,50)


def choix_couleur(nombre):
    if nombre %2==0:
        return 'black'
    else:
        return 'white'
    assert(choixCouleur(3)=='white')
    
def decalage (indice):
    if indice%6 == 0 or indice%6 == 1 or indice%6 == 2:
        return 20
    else:
        return -20
    
def carre_colore (tortue ,L, nombre):
    couleur= choix_couleur(nombre) #choisis entre lanc et noir selon la place de la case
    tortue.begin_fill() #commence le coloriage
    tortue.fillcolor(couleur) #remplit de la couleur choisie
    carre(fred,L)
    tortue.end_fill()
    return None 
    
    
solution2= carre_colore(fred, 100, 2)

