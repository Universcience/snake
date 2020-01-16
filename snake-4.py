#!/usr/bin/env python3

# Jeu du serpent, quatrième itération. (Déplacement sans collision.)
# Copyright (C) 2020 - Jérôme Kirman
# Ce programme est un logiciel libre ; voir les fichiers README.md et LICENSE.

import pygame, random
from collections import deque
from pygame.locals import *

# Constantes du jeu
lc, hc = 80, 60       # Hauteur/largeur (cases)
tc = 10               # Taille d'une case (pixels)
lf, hf = lc*tc, hc*tc # Hauteur/largeur (pixels)

# Pixel art
sol   = pygame.image.load("sand.png")
mur   = pygame.image.load("wall.png")
corps = pygame.image.load("body.png")
tete  = pygame.image.load("head.png")

# Retourne le rectangle correspondant à une case
def case(x, y):
	return (x*tc,y*tc,tc,tc)

# Génération de la carte en mémoire
niveau = []
for i in range(lc):
	niveau.append([])
	for j in range(hc):
		if i == 0 or i == lc-1 or j == 0 or j == hc-1:
			niveau[i].append("mur")
		else:
			niveau[i].append("sol")

# Placement du serpent
serpent = deque()
serpent.appendleft( (lc//2,hc//2) )
direction = 180
dx, dy = 0, 1

# Trucs importants
pygame.init()
fenetre = pygame.display.set_mode((lf,hf))
ips = pygame.time.Clock()

vitesse = 20    # Vitesse du jeu (en tics/s).

# Boucle principale
while True:
	# Vérification des évènements
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				print ("Touche ECHAP appuyée ; fin du jeu.")
				exit()
			elif event.key == K_UP:
				direction = 0
			elif event.key == K_DOWN:
				direction = 180
			elif event.key == K_LEFT:
				direction = 90
			elif event.key == K_RIGHT:
				direction = 270

	# Déplacement/croissance du serpent
	x,y = serpent[0]
	nx, ny = x+dx, y+dy
	serpent.appendleft((nx,ny))

	serpent.pop()

	# Dessin du niveau
	for i in range(lc):
		for j in range(hc):
			if niveau[i][j] == "mur":
				fenetre.blit(mur,case(i,j))
			else:
				fenetre.blit(sol,case(i,j))

	# Dessin du serpent (plus la tête, orientée)
	for s in serpent:
		x,y = s
		fenetre.blit(corps, case(x,y))
	x,y = serpent[0]
	fenetre.blit(pygame.transform.rotate(tete, direction), case(x,y))

	pygame.display.update()
	ips.tick(vitesse)
