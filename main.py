#!/usr/bin/env/python3
from sprite import Sprite
from dino import Dinosaur
from cactus import Cactus
from pterodactyl import Pterodactyl
from cloud import Cloud
from game import check_events, redraw_game_window
import pygame
import sys
import random

pygame.init()	# initialise pygame	

def create_objects(cacti, clouds, pterodactyls, score):
	images = ["big_cacti", "cacti", "triple_cactus"]
	# Creating objects like cactus, pterodactyls and clouds are done here
	# Use random module to have cacti, pterodactyls and clouds created at different times

	random_int = random.randint(1, 220)
	random_image = random.randint(0, 2)
	random_y_value = random.randint(0, 300)

	# if 0 < score % 10 < 3 or 5 < score % 10 < 7 or 7 < score % 10 < 9:
	if score % 5 == 0 or score % 27 == 0 or score % 39 == 0 or score % 56 == 0 or score % 137 == 0:
		if 5 < random_int < 10 or 64 < random_int < 70 or 165 < random_int < 179:
			if random_image == 0:
				random_image_number = random.randint(0, 3)
			elif random_image == 1:
				random_image_number = random.randint(0, 5)
			elif random_image == 2:
				random_image_number = random.randint(0, 0)

			cactus = Cactus(650, 300, 64, 64, 10, images[random_image], random_image_number)

			cacti.append(cactus)

	if score > 500:
		if score % 4 == 0 or score % 25 == 0 or score % 33 == 0 or score % 63 == 0 or score % 128 == 0:
			if 50 < random_int < 65 or 76 < random_int < 89 or 125 < random_int < 131:
				pterodactyl = Pterodactyl(650, random_y_value, 64, 64, 10)

				pterodactyls.append(pterodactyl)

	if score % 3 == 0 or score % 23 == 0 or score % 37 == 0 or score % 48 == 0 or score % 112 == 0:
		if 12 < random_int < 19 or 50 < random_int < 58 or 145 < random_int < 153:
			if 0 < random_y_value < 70:
				cloud = Cloud(650, random_y_value, 64, 64, 5)

				clouds.append(cloud)

	return cacti, clouds, pterodactyls

# Main loop
def main_loop():

	WINDOW_WIDTH = 650
	WINDOW_HEIGHT = 380

	game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))	# Set the game window size

	pygame.display.set_caption("Chrome Dinosaur Game")	# Set caption for what the game will be called

	clock = pygame.time.Clock()
	score = 0
	timer = 30
	shoot_loop = 0
	
	dino = Dinosaur(20, 300, 64, 64, 5, 300)	# create dino object
	ground = Sprite(0, 350, 64, 15, 0)

	cacti = []
	clouds = []
	pterodactyls = []
	fireballs = []

	run = True
	while run:
		clock.tick(timer + score // 1000)	# Set to 30fps then increment fps by score floor division of 1000

		if shoot_loop > 0:
			shoot_loop += 1
		if shoot_loop > 17:
			shoot_loop = 0

		run, score, shoot_loop = check_events(run, dino, game_window, ground, cacti, clouds, pterodactyls, clock, timer, score, shoot_loop, fireballs)

		cacti, clouds, pterodactyls = create_objects(cacti, clouds, pterodactyls, score)

		redraw_game_window(game_window, ground, dino, cacti, clouds, pterodactyls, clock, timer, score, fireballs)

		dino.check_collision(cacti, pterodactyls, game_window, score, fireballs)

		score += 1
		
if __name__ == '__main__':
	main_loop()

	pygame.quit()
	sys.exit()
