import pygame
from pygame.locals import *
import time
import settings
from apple import Apple
from snake import Snake

class Game: 
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface, settings.SNAKE_START_LENGTH)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.speed = settings.SPEED

    def reset(self):
        self.snake = Snake(self.surface, settings.SNAKE_START_LENGTH)
        self.apple = Apple(self.surface)
        self.speed = settings.SPEED        

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length - settings.SNAKE_START_LENGTH}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + settings.SIZE:
            if y1 >= y2 and y1 < y2 + settings.SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increment_length()
            self.apple.move()
            self.speed *= 0.9

        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"

    def show_game_over(self):
        self.surface.fill(((110,110,5)))
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f"Game over. Your score is {self.snake.length - settings.SNAKE_START_LENGTH}", True, (255, 255, 255))
        line2 = font.render(f"To play again press Enter", True, (255, 255, 255))
        line3 = font.render(f"To exit press Esc", True, (255, 255, 255))
        self.surface.blit(line1, (350, 300))
        self.surface.blit(line2, (350, 350))
        self.surface.blit(line3, (350, 400))
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key ==K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            if self.snake.direction != 'right':
                                self.snake.move_left()
                        if event.key == K_RIGHT:
                            if self.snake.direction != 'left':
                                self.snake.move_right()
                        if event.key == K_UP:
                            if self.snake.direction != 'down':
                                self.snake.move_up()
                        if event.key == K_DOWN:
                            if self.snake.direction != 'up':
                                self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(self.speed)
