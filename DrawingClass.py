

import pygame, os, sys
from EnemyClass import Enemy
from GameClass import Game
from BulletClass import Bullet
from PlayerClass import Player



current_dir = getattr(sys, '_MEIPASS', os.path.dirname(__file__))

BACKGROUND = pygame.image.load(os.path.join(current_dir, 'img', 'background.png'))


class Drawing:


    def __init__(self, window):

        self.window = window
        self.font = pygame.font.SysFont('comicsans', 50)
        self.HEIGHT = 600
        self.WIDTH = 800
      

    def drawing(self, game, player, enemies, FPS, puntos):

        self.window.blit(BACKGROUND, (0, 0))
        player.fire(self.window)

        for enemy in enemies[:]:
            enemy.draw(self.window)
        
        player.draw(self.window)

        game.draw_HUD()
        
        points_label = self.font.render(f'Points: {puntos}', 1, (255, 255, 255))
        self.window.blit(points_label, (self.WIDTH / 2 - points_label.get_width() / 2, 10))
        
        pygame.display.update()

