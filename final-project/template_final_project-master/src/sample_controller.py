import pygame

class GameController:
    def __init__(self):
        self.game_state = "MENU" 
        self.paused = False
        self.font = pygame.font.SysFont('Arial', 36)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.game_state == "MENU":
                if event.key == pygame.K_RETURN:
                    self.start_game()
            elif self.game_state == "PLAYING":
                if event.key == pygame.K_p:
                    self.toggle_pause()
                elif event.key == pygame.K_ESCAPE:
                    self.quit_game()
                elif event.key == pygame.K_LEFT:
                    self.move_player(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move_player(1, 0)
                elif event.key == pygame.K_UP:
                    self.move_player(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.move_player(0, 1)
            elif self.game_state == "PAUSED":
                if event.key == pygame.K_r:
                    self.toggle_pause()
                elif event.key == pygame.K_q:
                    self.quit_game()
            elif self.game_state == "GAME_OVER":
                if event.key == pygame.K_r:
                    self.start_game()

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.game_state = "PAUSED"
        else:
            self.game_state = "PLAYING"

    def start_game(self):
        self.game_state = "PLAYING"
        self.paused = False

    def quit_game(self):
        pygame.quit()
        quit()

    def update(self, screen):
        if self.game_state == "PAUSED":
            self.display_paused(screen)
        elif self.game_state == "GAME_OVER":
            self.display_game_over(screen)

    def display_paused(self, screen):
        paused_text = self.font.render("PAUSED", True, (255, 255, 255))
        screen.blit(paused_text, (screen.get_width() // 2 - paused_text.get_width() // 2, screen.get_height() // 2))

    def display_game_over(self, screen):
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2))

    def move_player(self, dx, dy):
        
        pass
