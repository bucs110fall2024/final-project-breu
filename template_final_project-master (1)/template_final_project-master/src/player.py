class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * 40
        self.rect.y = y * 40

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.x != new_x or self.y != new_y: 
            self.x = new_x
            self.y = new_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)