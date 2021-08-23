from sprite import Sprite
import pygame

class Cactus(Sprite):
	big_cacti_images = [pygame.image.load("Image_Sprites/big_cactus_1.png"), pygame.image.load("Image_Sprites/big_cactus_2.png"),
						pygame.image.load("Image_Sprites/big_cactus_3.png"), pygame.image.load("Image_Sprites/big_cactus_4.png")]
	cacti_images = [pygame.image.load("Image_Sprites/cactus_1.png"), pygame.image.load("Image_Sprites/cactus_2.png"),
					pygame.image.load("Image_Sprites/cactus_3.png"), pygame.image.load("Image_Sprites/cactus_4.png"),
					pygame.image.load("Image_Sprites/cactus_5.png"), pygame.image.load("Image_Sprites/cactus_6.png")]
	triple_cactus_image = [pygame.image.load("Image_Sprites/triple_cactus.png")]		
	
	def __init__(self, x, y, width, height, vel, image, image_number):
		super().__init__(x, y, width, height, vel)
		self.image = image
		self.image_number = image_number	# Value between 0 and 3 for big cacti, 0 and 5 for cacti, and 0 for triple cactus
		self.hitbox = (self.x - 6, self.y, 66, 60)	 # This is for a rectangle (x, y, width, height)

	def set_image(self, image):
		self.image = image

	def set_image_number(self, image_number):
		self.image_number = image_number

	def get_image(self):
		return self.image

	def get_image_number(self):
		return self.image_number

	def draw_cacti(self, game_window):
		if self.image == "big_cacti":
			game_window.blit(self.big_cacti_images[self.image_number], (self.x, self.y))
		elif self.image == "cacti":
			game_window.blit(self.cacti_images[self.image_number], (self.x, self.y))
		elif self.image == "triple_cactus":
			game_window.blit(self.triple_cactus_image[self.image_number], (self.x, self.y))

	def draw_hitbox(self, game_window, score):
		self.hitbox = (self.x - 6 - (score // 100), self.y, 66, 60)
		pygame.draw.rect(game_window, (255, 0, 0), self.hitbox, 2)