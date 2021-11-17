import pygame  # necessaire pour charger les images et les sons


class Joueur() : # classe pour pouvoir créer le vaisseau du joueur
    
    def __init__(self) :
        self.image = pygame.image.load('vaisseau.png')
        self.position = 400
        self.direction = "stop"
    
    def getPosition(self):
        return self.position
    
    def setDirection(self, direct):
        self.direction = direct
    
    def deplacer(self):
        if self.direction == "gauche" and self.position > 40 :
            self.position = self.position - 5
        if self.direction == "droite" and self.position < 760 :
            self.position = self.position + 5
       
            
class Balle():
    
    def __init__(self, joueur):
        self.image = pygame.image.load("balle.png")
        self.tireur = joueur.position
        self.depart = joueur
        self.hauteur = 500
        self.etat1 = "chargée"
        self.etat2 = "tirée"
        #self.joueur
        #self.image = pygame.image.load('balle.png')*

    def bouger(self):
        if self.etat == "chargée" :
            self.depart = self.tireur.position
        if self.etat == "tirée" :
            self.hauteur = self.hauteur - 10
        if self.hauteur < 10 :
            self.etat = "chargée"
            self.depart = self.tireur.position
            self.hauteur = 500
    
    
        
