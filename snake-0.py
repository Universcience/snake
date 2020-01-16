#!/usr/bin/env python3

# Jeu du serpent, version initiale (fenêtre vide).
# Copyright (C) 2020 - Jérôme Kirman
# Ce programme est un logiciel libre ; voir les ficheirs README.md et LICENSE.

import pygame
from pygame.locals import *

lf, hf = 50, 50

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

	pygame.display.update()
	ips.tick(vitesse)
