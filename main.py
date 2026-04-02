import pygame
from pygame import mixer
from GameClass import Game
import os
import sys
from PlayerClass import Player
from EnemyClass import Enemy
from DrawingClass import Drawing
from PantallaNombreClass import PantallaNombre
from MenuPrincipalClass import MenuPrincipal
from AcercaDeMenuClass import MenuAcercaDe
from MenuPuntajesClass import MenuPuntajes

# Obtener la ruta del directorio del script o del bundle
_BASE_PATH = getattr(sys, '_MEIPASS', os.path.dirname(__file__))

BACKGROUND = pygame.image.load(os.path.join(_BASE_PATH, 'img', 'background.png'))
ICON_IMAGE = pygame.image.load(os.path.join(_BASE_PATH, 'img', 'title_icon.png'))
TITLE = 'Space Invaders Hybridge'

PLAYER_IMAGE = pygame.image.load(os.path.join(_BASE_PATH, 'img', 'player_image.png'))
BULLET_IMAGE = pygame.image.load(os.path.join(_BASE_PATH, 'img', 'bullet_image.png'))

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON_IMAGE)

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


if not safe_load_music(os.path.join(_BASE_PATH, 'sounds', 'background_song1.mp3')):
    print("No se pudo cargar el sonido")

def main():
    puntaje = 0
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    try:
        mixer.music.play(-1)
    except:
        pass

    font = pygame.font.SysFont('comicsans', 50)
    game = Game(font, FPS, 3, WIN, WIDTH, HEIGHT, 0, clock)

    player_x = (WIDTH - PLAYER_IMAGE.get_width()) / 2
    player_y = 480
    player = Player(posicion_x=player_x, posicion_y=player_y, x_speed=5, y_speed=4)

    # template enemy: start with a moderate speed
    enemy_init = Enemy(speed=0.8)
    # initial wave size should be small to avoid screen overcrowding
    enemy_wave = 4
    MAX_ENEMIES_PER_WAVE = 12
    enemies = enemy_init.create(min(enemy_wave, MAX_ENEMIES_PER_WAVE))

    draw = Drawing(WIN)
    draw.drawing(game, player, enemies, FPS=60, puntos=puntaje)

    while run:
        clock.tick(FPS)

        if game.over():
            if puntaje > game.max_pun:
                sound = pygame.mixer.Sound(os.path.join(_BASE_PATH, "sounds", "ganar.mp3"))
                sound.play()
                PantallaNombre(puntaje, menu_principal)
                run = False
            else:
                menu_principal()
                run = False
            continue

        # get events once per frame and pass to game.escape
        events = pygame.event.get()
        if game.escape(events=events):
            run = False
            continue

        if len(enemies) == 0:
            game.level += 1
            enemy_wave += 1
            # increase the template speed and create a new wave from it
            enemy_init.increase_speed()
            player.increase_speed()
            enemies = enemy_init.create(amount=min(enemy_wave, MAX_ENEMIES_PER_WAVE))
            if game.level % 3 == 0:
                if player.max_amount_bullets < 10:
                    player.max_amount_bullets += 1
                if game.lives < 6:
                    game.lives += 1

        player.move()
        player.create_bullets()
        game.reload_bullet(len(player.bullets))
        player.cooldown()

        for enemy in enemies:
            # move enemy using its speed attribute if available
            try:
                enemy.move(enemy.speed)
            except Exception:
                # fallback to parameterless move if class defines it differently
                try:
                    enemy.move()
                except Exception:
                    pass

            if player.hit(enemy):
                enemies.remove(enemy)
                try:
                    player.fired_bullets.pop(0)
                except Exception:
                    pass
                crash_sound = pygame.mixer.Sound(os.path.join(_BASE_PATH, "sounds", "explosion.wav"))
                pygame.mixer.Sound.play(crash_sound)
                puntaje += 1

            if enemy.posicion_y + enemy.get_height() >= HEIGHT:
                game.lives -= 1
                enemies.remove(enemy)

        draw.drawing(game, player, enemies, FPS, puntaje)

def initGame():
    main()

def initPuntaje():
    menu_puntajes = MenuPuntajes(menu_principal).ejecutar()

def initAbout():
    menu_acercade = MenuAcercaDe(menu_principal).ejecutar()

def menu_principal():
    print("menu principal")
    menu_principal = MenuPrincipal(initGame, initPuntaje, initAbout).menu_principal()

menu_principal()