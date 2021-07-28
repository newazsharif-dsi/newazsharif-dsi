import pygame
class gun():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display_gun(self, screen, image):
        screen.blit(image, (self.x, self.y))
