import sys
import pygame

from ship import Ship
from settings import Settings

class AlienInvasion():
    """Class to manage game assets and behaviour"""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        
        self.ship = Ship(self)
    
    
    
    def run_game(self):
        """Main loop fopr the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            """Redraw the screen during each pass through the loop"""
            self.screen.fill(self.settings.bg_color)
            self.ship.blit()
                    
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()