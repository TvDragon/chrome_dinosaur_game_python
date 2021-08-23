from sprite import Sprite
import pygame

class Pterodactyl(Sprite):
	pterodactyl_images = [pygame.image.load("Image_Sprites/pterodactyl_1.png"), pygame.image.load("Image_Sprites/pterodactyl_2.png")]
	def __init__(self, x, y, width, height, vel):
		super().__init__(x, y, width, height, vel)
		self.hitbox = (self.x - 6, self.y, 66, 60)	 # This is for a rectangle (x, y, width, height)

	def draw_pterodactyl(self, game_window):
		# Draw dino character
		if self.get_walk_count() + 1 >= 6:
			self.set_walk_count(0)

		game_window.blit(self.pterodactyl_images[self.get_walk_count() // 3], (self.x, self.y))	# Take the floor division for which image to use
		self.set_walk_count(self.get_walk_count() + 1)

	def draw_hitbox(self, game_window, score):
		self.hitbox = (self.x - 6 - (score // 100), self.y, 66, 60)
		pygame.draw.rect(game_window, (255, 0, 0), self.hitbox, 2)