import pygame
from maze import Maze
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.maze = Maze()
        self.player = Player(self.maze.start_pos)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.player.handle_input(event.key)  

            self.update_game()
            self.render()

        pygame.quit()

    def update_game(self):
        if self.player.x == self.maze.goal_pos[0] and self.player.y == self.maze.goal_pos[1]:
            self.running = False 

    def render(self):
        self.screen.fill((0, 0, 0))
        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
