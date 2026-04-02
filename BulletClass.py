import pygame

class Bullet:


    def __init__(self, posicion_x, posicion_y, img):

        # use project standard names for coordinates
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)


    def draw(self, window):

        if self.img:
            window.blit(self.img, (self.posicion_x, self.posicion_y))
        else:
            print("No bullet image to draw.")


    def move(self, speed):

        # bullets should move up the screen: decrease posicion_y
        self.posicion_y -= speed
    

    
    def collision(self, obj):
        # support objects that use x/y or posicion_x/posicion_y
        obj_x = getattr(obj, 'posicion_x', None)
        obj_y = getattr(obj, 'posicion_y', None)
        if obj_x is None:
            obj_x = getattr(obj, 'x', None)
        if obj_y is None:
            obj_y = getattr(obj, 'y', None)

        if obj_x is None or obj_y is None:
            return False

        if not hasattr(obj, 'mask') or self.mask is None:
            return False

        offset = (int(self.posicion_x - obj_x - 30), int(self.posicion_y - obj_y - 20))
        return self.mask.overlap(obj.mask, offset) is not None