import pygame # importation de la librairie pygame
import sys # pour fermer correctement l'application
import space

### INITIALISATION ###
# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders") 
# chargement de l image de fond
fond = pygame.image.load('background.png')

 # # creation du joueur
# player = space.Joueur()

# ### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
#     # dessin du fond
    screen.blit(fond,(0,0))
    
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
#        # gestion du clavier
#         if event.type == pygame.KEYDOWN : # si une touche a été tapée
#             if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
#                 player.setDirection("gauche")  # définit la direction de déplacement
#             if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
#                 player.setDirection("droite")   # définit la direction de déplacement
 
#     ### Actualisation de la scene ###
#     # deplacement des objets
#     player.deplacer()
#     # dessins des objets        
#     screen.blit(player.image,(player.getPosition(),500))  # dessine le joueur à la position donné

    pygame.display.update() # pour mettre à jour l'écran
    

            
