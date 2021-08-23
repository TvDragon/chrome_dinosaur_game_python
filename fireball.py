from sprite import Sprite
import pygame

class Fireball(Sprite):
    fireball_image = [pygame.image.load("Image_Sprites/fireball_1.png")]

    def __init__(self, x, y, width, height, vel):
        super().__init__(x, y, width, height, vel)
        self.hitbox = (self.x - 6, self.y, 66, 60)	 # This is for a rectangle (x, y, width, height)

    def move_right(self, score):
        self.x += (self.vel + score // 150)
        self.set_x(self.x)

    def draw_fireball(self, game_window):
        game_window.blit(self.fireball_image[0], (self.x, self.y))

    def draw_hitbox(self, game_window, score):
        self.hitbox = (self.x - 6 - (score // 100), self.y, 66, 60)
        pygame.draw.rect(game_window, (255, 0, 0), self.hitbox, 2)