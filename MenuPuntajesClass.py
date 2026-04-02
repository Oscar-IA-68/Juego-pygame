import pygame
import sys
import os

class MenuPuntajes:
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    GRIS = (200, 200, 200)
    ROJO = (255, 0, 0)
    
    ANCHO = 800
    ALTO = 600
    
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mejores puntajes")
    
    @staticmethod
    def _get_scores_base_path():
        # En ejecutable usa la carpeta del .exe; en desarrollo usa la carpeta del script.
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        return os.path.dirname(os.path.abspath(__file__))

    def __init__(self, back_mtd):
        self.back_mtd = back_mtd
        
    def cargar_puntajes(self, archivo):
        puntajes = []
        ruta_archivo = os.path.join(self._get_scores_base_path(), archivo)
        try:
            with open(ruta_archivo, 'r') as file:
                for line in file:
                    raw = line.strip()
                    if not raw:
                        # skip empty lines
                        continue
                    if ',' not in raw:
                        print(f"Ignorando línea malformada en {archivo}.")
                        continue
                    nombre_part, puntaje_part = raw.split(',', 1)
                    nombre = nombre_part.strip()
                    try:
                        puntaje = int(puntaje_part.strip())
                    except ValueError:
                        print(f"Ignorando línea con puntaje no entero en {archivo}.")
                        continue
                    puntajes.append((nombre, puntaje))
        except FileNotFoundError:
            print(f"No se encontró el archivo {archivo}")
        return sorted(puntajes, key=lambda x: x[1], reverse=True)[:5]
    
    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img", nombre_archivo)
        return pygame.image.load(ruta).convert_alpha()
    
    def mostrar_texto(self, texto, font, color, superficie, x, y):
        texto_objeto = font.render(texto, True, color)
        rectangulo_texto = texto_objeto.get_rect()
        rectangulo_texto.center = (x, y)
        superficie.blit(texto_objeto, rectangulo_texto)
    
    def dibujar_boton(self, texto, font, color, superficie, x, y, ancho, alto):
        pygame.draw.rect(superficie, color, (x, y, ancho, alto))
        self.mostrar_texto(texto, font, self.NEGRO, superficie, x + ancho / 2, y + alto / 2)
    
    def mostrar_puntajes(self, puntajes):
        self.ventana.fill(self.NEGRO)
        fondo = self.cargar_imagen("menu_fondo.jpg")
        fondo = pygame.transform.scale(fondo, (self.ANCHO, self.ALTO))
        self.ventana.blit(fondo, (0, 0))
        self.mostrar_texto("Mejores Puntajes", pygame.font.Font(None, 48), self.BLANCO, self.ventana, self.ANCHO // 2, 50)
        self.mostrar_texto("Space Invaders Hybridge", pygame.font.Font(None, 36), self.BLANCO, self.ventana, self.ANCHO // 2, 120)
        
        if not puntajes:
            self.mostrar_texto("Aún no hay registros", pygame.font.Font(None, 36), self.ROJO, self.ventana, self.ANCHO // 2, self.ALTO // 2)
        else:
            y_offset = 220
            for i, (nombre, puntaje) in enumerate(puntajes, 1):
                color_texto = self.BLANCO if i == 1 else self.ROJO
                font_size = 42 if i == 1 else 36
                self.mostrar_texto(f"{i}. {nombre}: {puntaje}", pygame.font.Font(None, font_size), color_texto, self.ventana, self.ANCHO // 2, y_offset)
                y_offset += 60
        self.dibujar_boton("<", pygame.font.Font(None, 36), self.GRIS, self.ventana, 20, 20, 50, 50)
        pygame.display.update()
    
    def ejecutar(self):
        puntajes = self.cargar_puntajes("puntajes.txt")
        self.mostrar_puntajes(puntajes)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        if 20 <= x <= 70 and 20 <= y <= 70:
                            print("Acción atrás")
                            self.back_mtd()
                            return

"""
pygame.init()
menu_puntajes = MenuPuntajes(lambda: print("Volver al menú principal"))
menu_puntajes.ejecutar() 
"""