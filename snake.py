import pygame
import settings

class Snake:
    def __init__(self, surface, length):
        self.length = length
        self.parent_screen = surface
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [settings.SIZE] * length
        self.y = [settings.SIZE]  * length
        self.direction = 'down'

    def increment_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'
        self.draw()
    def move_right(self):
        self.direction = 'right'
        self.draw()
    def move_up(self):
        self.direction = 'up'
        self.draw()
    def move_down(self):
        self.direction = 'down'
        self.draw()

    def walk(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i -1]
            self.y[i] = self.y[i -1]

        if self.direction == 'up':
            if self.y[0] == 0:
                self.y[0] = settings.WINDOW_HEIGHT - settings.SIZE
            else:
                self.y[0] -= settings.SIZE

        if self.direction == 'down':
            if self.y[0] == settings.WINDOW_HEIGHT - settings.SIZE:
                self.y[0] = 0
            else:
                self.y[0] += settings.SIZE

        if self.direction == 'left':
            if self.x[0] == 0:
                self.x[0] = settings.WINDOW_WIDTH - settings.SIZE
            else:
                self.x[0] -= settings.SIZE

        if self.direction == 'right':
            if self.x[0] == settings.WINDOW_WIDTH - settings.SIZE:
                self.x[0] = 0
            else:
                self.x[0] += settings.SIZE

        self.draw()
