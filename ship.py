import pygame

class Ship:
    """Class that puts our ship on screen"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/ufo-flying-space-isolated-style-free-vector.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    def blit(self):
        """Sets a ship in position"""
        self.screen.blit(self.image, self.rect)