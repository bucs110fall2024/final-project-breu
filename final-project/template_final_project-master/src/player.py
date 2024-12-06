import pygame

class Player:
    def __init__(self, start_pos):
        self.x, self.y = start_pos
        self.color = (0, 255, 0)
        self.speed = 1

    def handle_input(self, key):
        if key == pygame.K_LEFT:
            self.move(-1, 0)
        elif key == pygame.K_RIGHT:
            self.move(1, 0)
        elif key == pygame.K_UP:
            self.move(0, -1)
        elif key == pygame.K_DOWN:
            self.move(0, 1)

    def move(self, dx, dy):

        self.x += dx
        self.y += dy

    def update(self, maze):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x * 30, self.y * 30, 30, 30))
