import pygame,os,sys
from pygame import mixer
from EnemyClass import Enemy
from GameClass import Game
from BulletClass import Bullet
from DrawingClass import Drawing
from ShipClass import Ship
from PlayerClass import Player



"""
# Inicializar pygame y variables globales
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ejemplo de Juego")

# Cargar imagen de bala
base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
BULLET_IMAGE = pygame.image.load(os.path.join(base_path, 'img', 'bullet_image.png'))

def main():

    
    run = True
    clock = pygame.time.Clock()
    puntos = 0

    # Crear instancia de la clase Drawing
    drawing = Drawing(WIN)

    # Crear instancias de la clase Enemy (velocidad=2, cantidad=5)
    enemies = Enemy(0, 0, 2, "blue").create(5)

    # Crear una instancia de la clase Game
    game = Game(pygame.font.SysFont('comicsans', 30), 60, 3, WIN, WIDTH, HEIGHT, bullets=4)

    # Crear un jugador de ejemplo
    player = Player(posicion_x=WIDTH//2, posicion_y=HEIGHT-80, health=100, x_speed=5, y_speed=5)
   
    # Crear una instancia de la clase Bullet como ejemplo (posicion_x, posicion_y)
    bullet_example = Bullet(400, 300, BULLET_IMAGE)

    while run:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for enemy in enemies:
            enemy.move(enemy.speed)

        # Dibujar en la pantalla usando la instancia de la clase Drawing
        drawing.drawing(game, player, enemies, 60, puntos)

        # Dibujar un ejemplo de bala en la pantalla
        bullet_example.draw(WIN)

        pygame.display.update()

    pygame.quit()
"""

"""

BACKGROUND = pygame.image.load(os.path.join('img', 'background.png'))
ICON_IMAGE = pygame.image.load(os.path.join('img', 'title_icon.png'))
TITLE = "Space Invaders Hybdrige"

WIDTH, HEIGHT = 800,600
PLAYER_IMAGE = pygame.image.load(os.path.join('img', 'player_image.png'))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON_IMAGE)

pygame.init()


def safe_load_music(path):
    try:
        mixer.init()
    except Exception:
        pass
    try:
        mixer.music.load(path)
        return True
    except Exception:
        return False

if not safe_load_music('sounds/background_song.mp3'):
    print("No se pudo cargar el sonido")

def main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    try:
        mixer.music.play(-1)
    except:
        pass
    font = pygame.font.SysFont('comicsans', 50)
    game = Game(font, FPS, 3, WIN, WIDTH, HEIGHT,0, clock )

    player_x = ((WIDTH)-(PLAYER_IMAGE.get_width()))/2
    player_y = 480

    player = Player(posicion_x=player_x, posicion_y=player_y, x_speed=5, y_speed=4)

    enemy_init = Enemy(posicion_x=0, posicion_y=0, speed=0.8, color="blue")
    enemy_wave = 4
    enemies = enemy_init.create(enemy_wave)

    draw = Drawing(WIN)

    draw.drawing(game, player, enemies, FPS=FPS, puntos=0)

    while run:

        clock.tick(FPS)
        events = pygame.event.get()
        # check for quit events
        if game.over():
            run = False
        if game.escape(events=events):
            run = False

        if len(enemies) == 0:
            game.level += 1
            enemy_wave += 1
            enemy_init.increase_speed()
            player.increase_speed()
            enemies = enemy_init.create(amount=enemy_wave)
        
        if game.level % 3 == 0:
            if player.max_amount_bullets < 10:
                player.max_amount_bullets += 1
            if game.lives < 6:
                game.lives += 1

        player.move()
        player.create_bullets()
        player.fire(WIN)
        game.reload_bullet(len(player.bullets))
        player.cooldown()

        for enemy in enemies:
            enemy.move(enemy.speed)
            if player.hit(enemy):
                enemies.remove(enemy)
                player.fired_bullets.pop(0)
            if enemy.posicion_y + enemy.get_height() >= HEIGHT:
                game.lives -= 1
                enemies.remove(enemy)
        draw.drawing(game, player, enemies, FPS, puntos=game.level*10)
        
"""
if __name__ == "__main__":
    main()
