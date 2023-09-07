import pygame

class Ship:
    """Class that puts our ship on screen"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('/home/domen/Desktop/Quantecum/Alien-Invasion-Game/images/ufo-flying-space-isolated-style-free-vector.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
    def update(self):
        if self.moving_right:
            self.rect.x += 1
    def blitme(self):
        """Sets a ship in position"""
        self.screen.blit(self.image, self.rect)