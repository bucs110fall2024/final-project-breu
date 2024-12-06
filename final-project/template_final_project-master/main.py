import pygame
from game import Game

def main_menu(screen):
    font = pygame.font.SysFont('Arial', 36)
    screen.fill((0, 0, 0))
    title_text = font.render("Welcome to the Maze Game", True, (255, 255, 255))
    start_text = font.render("Press Enter to Start", True, (255, 255, 255))

    screen.blit(title_text, (250, 200))
    screen.blit(start_text, (250, 300))
    pygame.display.update()

   
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                waiting_for_input = False
                return

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Maze Game')

    main_menu(screen)

    game = Game(screen)
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()
