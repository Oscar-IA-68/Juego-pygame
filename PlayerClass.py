import pygame
import sys
import os
from ShipClass import Ship
from BulletClass import Bullet


class Player(Ship):


    def __init__(self, posicion_x, posicion_y, health = 100, x_speed=5, y_speed=5):
        super().__init__(posicion_x, posicion_y, health)
        self.x_speed = x_speed
        self.y_speed = y_speed
        # cargar imágenes y mask
        self.ship_img = pygame.image.load(os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(__file__)), 'img', 'player_image.png'))
        self.bullet_img = pygame.image.load(os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(__file__)), 'img', 'bullet_image.png'))
        self.mask = pygame.mask.from_surface(self.ship_img)

        # atributos de juego
        self.max_health = health
        self.WIDTH = 800
        self.HEIGHT = 600
        self.bullet_speed = 5
        self.creation_cooldown_counter = 0
        self.max_amount_bullets = 3
        self.bullets = []
        self.fired_bullets = []
        self.bullet_cooldown_counter = 0



    def move(self):
        
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (self.posicion_y > 0):
            self.posicion_y -= self.y_speed
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (self.posicion_y < self.HEIGHT-self.ship_img.get_height()-60):
            self.posicion_y += self.y_speed
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (self.posicion_x < self.WIDTH - self.ship_img.get_width()):
            self.posicion_x += self.x_speed
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (self.posicion_x > 0):
            self.posicion_x -= self.x_speed



    def increase_speed(self):

        if self.x_speed < 10:
            self.x_speed += 1.25
            self.y_speed += 1.25
        elif self.x_speed >= 10:
            self.x_speed = 10
            self.y_speed = 10
        if self.cool_down > 25:
            self.cool_down *= 0.9



    def fire(self, window):

        keys = pygame.key.get_pressed()
        
        if (keys[pygame.K_SPACE]) and (len(self.bullets) > 0) and (self.bullet_cooldown_counter == 0):
            self.bullets[-1].posicion_x = self.posicion_x + (self.ship_img.get_width() - self.bullet_img.get_width()) / 2
            self.bullets[-1].posicion_y = self.posicion_y - 10
            self.fired_bullets.append(self.bullets.pop())
            self.bullet_cooldown_counter = 1
            self.creation_cooldown_counter = 1
            
        for i in range(len(self.fired_bullets)):
            self.fired_bullets[i].move(self.bullet_speed)
            self.fired_bullets[i].draw(window)




    def hit(self, enemy):

        for i in range(len(self.fired_bullets)):
            self.creation_cooldown_counter = self.cool_down * 0.8
            return self.fired_bullets[i].collision(enemy)
    


    def create_bullets(self):

        if (len(self.bullets) < self.max_amount_bullets) and (self.creation_cooldown_counter == 0):
            # spawn bullet at top-center of the ship
            bx = self.posicion_x + (self.ship_img.get_width() - self.bullet_img.get_width()) / 2
            by = self.posicion_y - self.bullet_img.get_height()
            bullet = Bullet(bx, by, self.bullet_img)
            self.bullets.append(bullet)
            self.creation_cooldown_counter = 1
        # remove bullets that went off-screen
        for bullet in list(self.fired_bullets):
            if getattr(bullet, 'posicion_y', getattr(bullet, 'y', 0)) <= -40:
                try:
                    self.fired_bullets.remove(bullet)
                except ValueError:
                    pass
    


    def cooldown(self):

        if self.bullet_cooldown_counter >= 20:
            self.bullet_cooldown_counter = 0
        elif self.bullet_cooldown_counter > 0:
            self.bullet_cooldown_counter += 1
          
        if self.creation_cooldown_counter >= 20:
            self.creation_cooldown_counter = 0
        elif self.creation_cooldown_counter > 0:
            self.creation_cooldown_counter += 1   