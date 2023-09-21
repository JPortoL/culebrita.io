import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
GRIS = (169, 169, 169)
GRIS_CLARO = (211, 211, 211)
NEGRO = (0, 0, 0)

GREEN = (0, 255, 0)

# Configuración de la pantalla
ANCHO = 390
ALTO = 420
TAMANO_CELDA = 30
FILAS = 13
COLUMNAS = 13

WIDTH, HEIGHT = 390, 420
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Culebrita")

font = pygame.font.Font(None, 28)

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                # Iniciar el juego cuando se presiona la barra espaciadora
                    juego()

    # Dibujar el fondo del menú
        screen.fill(BLANCO)

        # Dibujar el título
        draw_text("Culebrita", WIDTH // 2, HEIGHT // 4, GREEN)

        # Instrucciones
        draw_text("Presiona la barra espaciadora para jugar", WIDTH // 2, HEIGHT // 2, GREEN)

        pygame.display.flip()

# Inicializar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")

# Función para dibujar la cuadrícula
def dibujar_cuadricula():
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            pygame.draw.rect(pantalla, GRIS, (columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA), 1)

def generar_posicion_manzana(serpiente):
    while True:
        manzana_x = random.randint(0, COLUMNAS - 1)
        manzana_y = random.randint(0, FILAS - 1)
        if (manzana_x, manzana_y) not in serpiente:
            return manzana_x, manzana_y

# Función principal del juego
def juego():
    cabeza_x = COLUMNAS // 2
    cabeza_y = FILAS // 2
    serpiente = [(cabeza_x, cabeza_y), (cabeza_x , cabeza_y+1), (cabeza_x , cabeza_y+2)]
    direccion = None

    manzana_x, manzana_y = 9,3

    puntuacion = 0  # Inicializar la puntuación

    perdido = False
 
    while not perdido:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if direccion is None:
            # Esperar a que el jugador presione una tecla para comenzar a mover la serpiente
            if any(keys):
                if keys[pygame.K_LEFT]:
                    direccion = 'izquierda'
                elif keys[pygame.K_RIGHT]:
                    direccion = 'derecha'
                elif keys[pygame.K_UP]:
                    direccion = 'arriba'
               
                
        else:
            # Movimiento de la serpiente después de comenzar el juego
            if keys[pygame.K_LEFT] and direccion != 'derecha':
                direccion = 'izquierda'
            elif keys[pygame.K_RIGHT] and direccion != 'izquierda':
                direccion = 'derecha'
            elif keys[pygame.K_UP] and direccion != 'abajo':
                direccion = 'arriba'
            elif keys[pygame.K_DOWN] and direccion != 'arriba':
                direccion = 'abajo'
            elif keys[pygame.K_SPACE]:
                direccion = None

            if direccion == 'izquierda':
                cabeza_x -= 1
            elif direccion == 'derecha':
                cabeza_x += 1
            elif direccion == 'arriba':
                cabeza_y -= 1
            elif direccion == 'abajo':
                cabeza_y += 1
            
            # Verificar colisión con los bordes
            if cabeza_x < 0 or cabeza_x >= COLUMNAS or cabeza_y < 0 or cabeza_y >= FILAS:
                perdido = True            

            # Verificar colisión con la serpiente
            if (cabeza_x, cabeza_y) in serpiente[1:]:
                perdido = True

            serpiente.insert(0, (cabeza_x, cabeza_y))

            # Comer la manzana
            if cabeza_x == manzana_x and cabeza_y == manzana_y:
                manzana_x, manzana_y = generar_posicion_manzana(serpiente)
                puntuacion += 1  # Incrementar la puntuación
            else:
                serpiente.pop()

        # Dibujar fondo
        pantalla.fill(BLANCO)

        # Dibujar serpiente
        for segmento in serpiente:
            if segmento == serpiente[0]:
                pygame.draw.ellipse(pantalla, GRIS, (segmento[0] * TAMANO_CELDA, segmento[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
            else:
                pygame.draw.ellipse(pantalla, GRIS_CLARO, (segmento[0] * TAMANO_CELDA, segmento[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
        # Dibujar manzana
        pygame.draw.rect(pantalla, NEGRO, (manzana_x * TAMANO_CELDA, manzana_y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))

        # Dibujar cuadrícula
        dibujar_cuadricula()

        # Mostrar puntuación en la pantalla
        fuente = pygame.font.Font(None, 36)
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, NEGRO)
        pantalla.blit(texto_puntuacion, (10, 395))

        pygame.display.update()
        pygame.time.delay(90)

    #Mostrar mensaje de "¡Perdiste!" en la pantalla
    pantalla.fill(BLANCO)
    fuente = pygame.font.Font(None, 36)
    mensaje = fuente.render("¡Perdiste!", True, NEGRO)
    mensaje2 = fuente.render("que maloooo", True, NEGRO)
    texto_puntuacion = fuente.render(f"Puntuación final: {puntuacion}", True, NEGRO)
    pantalla.blit(mensaje, (ANCHO // 2 - mensaje.get_width() // 2, ALTO // 2 - mensaje.get_height() // 2))
    pantalla.blit(mensaje2, (ANCHO // 2 - mensaje2.get_width() // 2, ALTO // 2 - mensaje2.get_height() // 2 + mensaje.get_height()))
    pantalla.blit(texto_puntuacion, (ANCHO // 2 - texto_puntuacion.get_width() // 2, ALTO // 2 + mensaje.get_height() + mensaje2.get_height()))
    pygame.display.update()
    pygame.time.delay(2000)  # Esperar 2 segundos antes de salir

main_menu()
