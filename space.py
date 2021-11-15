import pygame  # necessaire pour charger les images et les sons


class joueur (): #creation du vaisseau
        
        def _init_(self):
            self.image = pygame.image.load('vaisseau.png')
            self.position = 400
            self.direction
            
        def setDiretion(self, dir):
            self.direction = dir
            
        def getPosition(self):
            return self.position
        
        def deplacer(self):
            if self.direction == 'droite':
                self.position = self.position + 10
            else:
                self.position = self.position - 10
            
            #if self.direction == "gauche" and 0 <= self.position:
            #self.position = self.position - 5
            #elif self.direction == "droite" and self.position <= 800-60:
            #self.position = self.position + 5
            