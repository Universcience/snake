#!/usr/bin/env python3

# Jeu du serpent, version finale.
# Copyright (C) 2020 - Jérôme Kirman
# Ce programme est un logiciel libre ; voir les ficheirs README.md et LICENSE.

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
boost = pygame.image.load("star.png")
corps = pygame.image.load("body.png")
tete  = pygame.image.load("head.png")

# Retourne le rectangle correspondant à une case
def case(x, y):
	return (x*tc,y*tc,tc,tc)

# Retourne True lorsque la case (x, y) est traversable, False sinon.
def case_libre(x, y):
	if niveau[x][y] == "mur":
		return False
	for s in serpent:
		if s == (x,y):
			return False
	return True

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

# Placement d'un bonus au sol au hasard
def choisir_case_bonus():
	while True:
		x,y = (random.randrange(lc), random.randrange(hc))
		if case_libre(x,y):
			return x,y

bonus = choisir_case_bonus()

# Trucs importants
pygame.init()
fenetre = pygame.display.set_mode((lf,hf))
ips = pygame.time.Clock()

vitesse = 20    # Vitesse du jeu (en tics/s).
croissance = 10 # Croissance restant à effectuer

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
				dx, dy = 0, -1
			elif event.key == K_DOWN:
				direction = 180
				dx, dy = 0, 1
			elif event.key == K_LEFT:
				direction = 90
				dx, dy = -1, 0
			elif event.key == K_RIGHT:
				direction = 270
				dx, dy = 1, 0

	# Déplacement/croissance du serpent
	x,y = serpent[0]
	nx, ny = x+dx, y+dy
	if (not case_libre(nx, ny)):
		print ("Game over !")
		exit()
	else:
		serpent.appendleft((nx,ny))

	if croissance == 0:
		serpent.pop()
	else:
		croissance -= 1

	# Repas ?
	if serpent[0] == bonus:
		bonus = choisir_case_bonus()
		croissance += 3

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

	# Dessin du bonus
	x,y = bonus
	fenetre.blit(boost, case(x,y))

	pygame.display.update()
	ips.tick(vitesse)
