from sprite import Sprite
import pygame
import sys
import time
import datetime

class Dinosaur(Sprite):
	dino_run = [pygame.image.load("Image_Sprites/dino_run_1.png"), pygame.image.load("Image_Sprites/dino_run_2.png"), pygame.image.load("Image_Sprites/dino_run_3.png")]
	dino_duck = [pygame.image.load("Image_Sprites/dino_duck_1.png"), pygame.image.load("Image_Sprites/dino_duck_2.png")]

	def __init__(self, x, y, width, height, vel, max_y):
		super().__init__(x, y, width, height, vel)
		self.max_y = max_y
		self.is_jump = False
		self.is_duck = False
		self.jump_count = 10
		self.hitbox = (self.x, self.y, 60, 60)	 # This is for a rectangle (x, y, width, height)

	def get_max_y(self):
		return self.max_y

	def jump(self):
			if self.jump_count >= -10:
				neg = 1
				if self.jump_count < 0:
					neg = -1

				self.y -= (self.jump_count ** 2) / 2 * neg
				self.set_y(self.y)
				self.jump_count -= 1
			else:
				self.is_jump = False
				self.jump_count = 10

	def draw_run(self, game_window):
		# Draw dino character
		if self.get_walk_count() + 1 >= 9:
			self.set_walk_count(0)

		game_window.blit(self.dino_run[self.get_walk_count() // 3], (self.x, self.y))	# Take the floor division for which image to use
		self.set_walk_count(self.get_walk_count() + 1)

	def duck(self, game_window, ground, cacti, clouds, pterodactyls, clock, timer, score, fireballs):
		if self.is_jump:	# Dino moves down quickly onto floor
			if self.y < self.max_y:
				self.y += (self.vel + score // 100)
				if self.y >= self.max_y:
					self.y = self.max_y
				self.set_y(self.y)

		if self.y >= self.max_y:
			self.is_jump = False
			self.jump_count = 10
		return score

	def draw_duck(self, game_window):
		if self.get_walk_count() + 1 >= 6:
			self.set_walk_count(0)

		game_window.blit(self.dino_duck[self.get_walk_count() // 3], (self.x, self.y))	# Take the floor division for which image to use
		self.set_walk_count(self.get_walk_count() + 1)

	def draw_hitbox(self, game_window):
		self.hitbox = (self.x, self.y, 60, 60)
		pygame.draw.rect(game_window, (255, 0, 0), self.hitbox, 2)

	def check_collision(self, cacti, pterodactyls, game_window, score, fireballs):
		dino_left = self.get_x()
		dino_right = self.get_x() + self.get_width()
		dino_top = self.get_y()
		dino_bottom = self.get_y() + self.get_height()

		for fireball in fireballs:
			fireball_left = fireball.get_x()
			fireball_right = fireball.get_x() + fireball.get_width()
			fireball_top = fireball.get_y()
			fireball_bottom = fireball.get_y() + fireball.get_height()

			for cactus in cacti:
				cactus_left = cactus.get_x()
				cactus_right = cactus.get_x() + cactus.get_width()
				cactus_top = cactus.get_y()
				cactus_bottom = cactus.get_y() + cactus.get_height()

				# Check for fireball collision with cactus
				try:
					if (fireball_left <= cactus_left <= fireball_right and fireball_top <= cactus_top <= fireball_bottom) or (fireball_left <= cactus_left <= fireball_right and fireball_top <= cactus_bottom <= fireball_bottom):
						fireballs.pop(fireballs.index(fireball))
						cacti.pop(cacti.index(cactus))

					elif (fireball_left <= cactus_right <= fireball_right and fireball_top <= cactus_top <= fireball_bottom) or (fireball_left <= cactus_right <= fireball_right and fireball_top <= cactus_bottom <= fireball_bottom):
						fireballs.pop(fireballs.index(fireball))
						cacti.pop(cacti.index(cactus))
				except ValueError:
					pass

			for pterodactyl in pterodactyls:
				pterodactyl_left = pterodactyl.get_x()
				pterodactyl_right = pterodactyl.get_x() + pterodactyl.get_width()
				pterodactyl_top = pterodactyl.get_y()
				pterodactyl_bottom = pterodactyl.get_y() + pterodactyl.get_height()

				# Check for fireball collision with pterodactyl
				try:
					if (fireball_left <= pterodactyl_left <= fireball_right and fireball_top <= pterodactyl_top <= fireball_bottom) or (fireball_left <= pterodactyl_left <= fireball_right and fireball_top <= pterodactyl_bottom <= fireball_bottom):
						fireballs.pop(fireballs.index(fireball))
						pterodactyls.pop(pterodactyls.index(pterodactyl))

					elif (fireball_left < pterodactyl_right <= fireball_right and fireball_top <= pterodactyl_top <= fireball_bottom) or (fireball_left <= pterodactyl_right <= fireball_right and fireball_top <= pterodactyl_bottom <= fireball_bottom):
						fireballs.pop(fireballs.index(fireball))
						pterodactyls.pop(pterodactyls.index(pterodactyl))
				except ValueError:
					pass

		for cactus in cacti:
			cactus_left = cactus.get_x()
			cactus_right = cactus.get_x() + cactus.get_width()
			cactus_top = cactus.get_y()
			cactus_bottom = cactus.get_y() + cactus.get_height()

			# Check for dinosaur collision with cactus
			if (dino_left <= cactus_left <= dino_right and dino_top <= cactus_top <= dino_bottom) or (dino_left <= cactus_left <= dino_right and dino_top <= cactus_bottom <= dino_bottom):
				self.game_over(game_window, score)

			elif (dino_left <= cactus_right <= dino_right and dino_top <= cactus_top <= dino_bottom) or (dino_left <= cactus_right <= dino_right and dino_top <= cactus_bottom <= dino_bottom):
				self.game_over(game_window, score)

		for pterodactyl in pterodactyls:
			pterodactyl_left = pterodactyl.get_x()
			pterodactyl_right = pterodactyl.get_x() + pterodactyl.get_width()
			pterodactyl_top = pterodactyl.get_y()
			pterodactyl_bottom = pterodactyl.get_y() + pterodactyl.get_height()

			# Check for dinosaur collision with pterodactyl
			if (dino_left <= pterodactyl_left <= dino_right and dino_top <= pterodactyl_top <= dino_bottom) or (dino_left <= pterodactyl_left <= dino_right and dino_top <= pterodactyl_bottom <= dino_bottom):
				self.game_over(game_window, score)

			elif (dino_left < pterodactyl_right <= dino_right and dino_top <= pterodactyl_top <= dino_bottom) or (dino_left <= pterodactyl_right <= dino_right and dino_top <= pterodactyl_bottom <= dino_bottom):
				self.game_over(game_window, score)

	def game_over(self, game_window, score):
		game_over_images = [pygame.image.load("Image_Sprites/game_over_text.png")]

		game_over_text = Sprite(25, 50, 600, 129, 0)
		# game_over_image = Sprite(0, )

		game_window.fill((255,255,255)) # Create white background
		game_window.blit(game_over_images[0], (game_over_text.get_x(), game_over_text.get_y()))

		font = pygame.font.SysFont(None, 50)			# SysFont creates a font object from available pygame fonts
		BLACK = (0, 0, 0)
		player_score = font.render(f"Score: {str(score)}", True, BLACK)
		game_window.blit(player_score, (200, 200))

		pygame.display.update() # Update the display

		time.sleep(2)

		pygame.quit()

		sys.exit()
