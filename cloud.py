from sprite import Sprite
import pygame

class Cloud(Sprite):
    cloud_image = [pygame.image.load("Image_Sprites/cloud.png")]

    def __init__(self, x, y, width, height, vel):
        super().__init__(x, y, width, height, vel)

    def draw_cloud(self, game_window):
        game_window.blit(self.cloud_image[0], (self.x, self.y))