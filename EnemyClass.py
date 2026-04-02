import pygame, random, os, sys
from ShipClass import Ship


current_dir = getattr(sys, '_MEIPASS', os.path.dirname(__file__))

BULLET_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'bullet_image.png'))
ENEMY_BLUE_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'enemy_blue_image.png'))
ENEMY_GREEN_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'enemy_green_image.png'))
ENEMY_PURPLE_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'enemy_purple_image.png'))
SHOT_BLUE_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'shot_blue.png'))
SHOT_GREEN_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'shot_green.png'))
SHOT_PURPLE_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'shot_purple.png'))



class Enemy(Ship):


    COLOR_MAP = {

        "blue": (ENEMY_BLUE_IMAGE, SHOT_BLUE_IMAGE),
        "green": (ENEMY_GREEN_IMAGE, SHOT_GREEN_IMAGE),
        "purple": (ENEMY_PURPLE_IMAGE, SHOT_PURPLE_IMAGE)
    }


    def __init__(self, posicion_x=0, posicion_y=0, speed=1, color="blue", health=100):

        # allow creating a template Enemy with only speed (or defaults)
        super().__init__(posicion_x, posicion_y, health)
        # ensure color is valid
        if color not in self.COLOR_MAP:
            color = "blue"
        self.ship_img, self.bullet_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.speed = speed
        self.WIDTH = 800
        self.HEIGHT = 600


    def move(self, vel):

        self.posicion_y += vel
    

    def create(self, amount):
    
        enemies = []
        min_gap = ENEMY_BLUE_IMAGE.get_width() + 20

        for i in range(amount):
            # try to find a non-overlapping x position
            attempt = 0
            max_attempts = 50
            while True:
                x = random.randrange(20, self.WIDTH - ENEMY_BLUE_IMAGE.get_width() - 20)
                # check horizontal distance against existing enemies
                too_close = False
                for e in enemies:
                    if abs(x - e.posicion_x) < min_gap:
                        too_close = True
                        break
                if not too_close or attempt >= max_attempts:
                    break
                attempt += 1

            # y spawn above the screen with some variation
            y = random.randrange(-1000 - i*50, -100 - i*10)
            color = random.choice(["blue", "green", "purple"])
            speed = self.speed
            enemy = Enemy(posicion_x=x, posicion_y=y, color=color, speed=speed)
            enemies.append(enemy)
        return enemies
    

    def increase_speed(self):

        self.speed *= 1.02


