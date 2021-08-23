import pygame

class Sprite:
	def __init__(self, x, y, width, height, vel):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel
		self.walk_count = 0
		self.show_hitbox = False

	def set_x(self, x):
		self.x = x

	def set_y(self, y):
		self.y = y

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def set_vel(self, vel):
		self.vel = vel

	def set_walk_count(self, walk_count):
		self.walk_count = walk_count

	def set_show_hitbox(self, show_hitbox):
		self.show_hitbox = show_hitbox

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def get_vel(self):
		return self.vel

	def get_walk_count(self):
		return self.walk_count

	def get_show_hitbox(self):
		return self.show_hitbox

	def move_left(self, score):
		self.x -= (self.vel + score // 100)
		self.set_x(self.x)

	def draw_ground(self, game_window):
		ground_image = [pygame.image.load("Image_Sprites/floor_shorter.png")]
		game_window.blit(ground_image[0], (self.x, self.y))