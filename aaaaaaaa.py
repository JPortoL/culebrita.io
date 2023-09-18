import pygame
import random

# Inicializar pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
GRIS = (169, 169, 169)
GRIS_CLARO = (211, 211, 211)
NEGRO = (0, 0, 0)

# Configuración de la pantalla
ANCHO = 400
ALTO = 400
TAMANO_CELDA = 30
FILAS = 13
COLUMNAS = 13

# Inicializar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")

# Función para dibujar la cuadrícula
def dibujar_cuadricula():
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            pygame.draw.rect(pantalla, GRIS, (columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA), 1)

# Función principal del juego
def juego():
    cabeza_x = COLUMNAS // 2
    cabeza_y = FILAS // 2
    serpiente = [(cabeza_x, cabeza_y), (cabeza_x - 1, cabeza_y), (cabeza_x - 2, cabeza_y)]
    direccion = "arriba"

    manzana_x = random.randint(0, COLUMNAS - 1)
    manzana_y = random.randint(0, FILAS - 1)

    
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and direccion != 'derecha':
            direccion = 'izquierda'
        elif keys[pygame.K_RIGHT] and direccion != 'izquierda':
            direccion = 'derecha'
        elif keys[pygame.K_UP] and direccion != 'abajo':
            direccion = 'arriba'
        elif keys[pygame.K_DOWN] and direccion != 'arriba':
            direccion = 'abajo'

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
            pygame.quit()
            quit()

        # Verificar colisión con la serpiente
        if (cabeza_x, cabeza_y) in serpiente[1:]:
            pygame.quit()
            quit()

        serpiente.insert(0, (cabeza_x, cabeza_y))

        # Comer la manzana
        if cabeza_x == manzana_x and cabeza_y == manzana_y:
            manzana_x = random.randint(0, COLUMNAS - 1)
            manzana_y = random.randint(0, FILAS - 1)
        else:
            serpiente.pop()

        # Dibujar fondo
        pantalla.fill(BLANCO)

        # Dibujar serpiente
        for segmento in serpiente:
            if segmento == serpiente[0]:
                pygame.draw.rect(pantalla, GRIS, (segmento[0] * TAMANO_CELDA, segmento[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
            else:
                pygame.draw.rect(pantalla, GRIS_CLARO, (segmento[0] * TAMANO_CELDA, segmento[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
        # Dibujar manzana
        pygame.draw.rect(pantalla, NEGRO, (manzana_x * TAMANO_CELDA, manzana_y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))

        # Dibujar cuadrícula
        dibujar_cuadricula()

        pygame.display.update()
        pygame.time.delay(100)

juego()
