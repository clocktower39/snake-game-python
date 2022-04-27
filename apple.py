import pygame
import random
import settings

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('resources/apple.jpg').convert()
        self.parent_screen = parent_screen
        self.x = settings.SIZE * 3
        self.y = settings.SIZE * 3
        
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0,24) * settings.SIZE
        self.y = random.randint(0,19) * settings.SIZE