# Space Invaders Hybridge

Juego estilo Space Invaders desarrollado con Python y Pygame, con enfoque didáctico en Programación Orientada a Objetos (POO).

## Características

- Menú principal con navegación por teclado.
- Juego con oleadas de enemigos y dificultad progresiva.
- Sistema de vidas, nivel y puntaje en pantalla.
- Registro de puntajes y pantalla de mejores resultados.
- Pantalla "Acerca de" con acceso al sitio de Hybridge.
- Compatibilidad con ejecución normal de Python y ejecutable generado con PyInstaller.

## Tecnologías

- Python 3.10 o superior
- Pygame
- PyInstaller (opcional, para generar ejecutable)

## Estructura del proyecto

- `main.py`: punto de entrada y ciclo principal del juego.
- `GameClass.py`: lógica general del estado del juego (vidas, nivel, HUD).
- `PlayerClass.py`: comportamiento del jugador y disparos.
- `EnemyClass.py`: comportamiento de enemigos y generación de oleadas.
- `ShipClass.py`: clase base de naves.
- `BulletClass.py`: lógica de proyectiles y colisiones.
- `DrawingClass.py`: renderizado de escena y HUD.
- `MenuPrincipalClass.py`: menú principal.
- `MenuPuntajesClass.py`: menú de mejores puntajes.
- `PantallaNombreClass.py`: captura de nombre cuando hay nuevo récord.
- `AcercaDeMenuClass.py`: pantalla informativa.
- `img/`: recursos gráficos.
- `sounds/`: recursos de audio.
- `main.spec`: configuración de PyInstaller.

## Requisitos

1. Tener Python instalado.
2. Instalar dependencias:

```bash
pip install pygame
```

## Cómo ejecutar

Desde la raíz del proyecto:

```bash
python main.py
```

## Controles

- Menú principal:
  - Flecha Arriba/Abajo: cambiar opción
  - Enter: seleccionar
- Juego:
  - Movimiento: `WASD` o flechas
  - Disparo: barra espaciadora
- Menús secundarios:
  - Clic en botón `<` para volver

## Puntajes

- El juego guarda puntajes en un archivo local `puntajes.txt`.
- Ese archivo se ignora en Git para no compartir datos personales/locales.
- Si no existe, se crea automáticamente al registrar un nuevo puntaje.

## Empaquetar ejecutable (opcional)

Con PyInstaller instalado:

```bash
pyinstaller main.spec
```

El ejecutable se genera en `dist/`.

## Solución de problemas

- Si no se escucha audio, verifica que los archivos en `sounds/` existan y sean compatibles.
- Si falta una imagen o sonido, confirma que las carpetas `img/` y `sounds/` estén en la raíz del proyecto.
- Si usas el ejecutable, evita mover recursos fuera de las rutas configuradas en `main.spec`.

## Licencia

Este proyecto no define una licencia explícita. Si lo vas a reutilizar o distribuir, agrega un archivo de licencia adecuado.
