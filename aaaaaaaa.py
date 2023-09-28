import pygame
import random
import sys

# Inicializar pygame
pygame.init()

#(O(1))  ----- TODAS LAS VARIABLES

# Definir colores
BLANCO = (255, 255, 255)
GRIS = (169, 169, 169)
GRIS_CLARO = (190, 190, 190)
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

# O(1) HASTA ACA



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
        draw_text("Culebrita.io", WIDTH // 2, HEIGHT // 4, GREEN)

        # Instrucciones
        draw_text("Presiona la barra espaciadora para jugar", WIDTH // 2, HEIGHT // 2, GREEN)

        pygame.display.flip()

# Inicializar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Culebrita")

# Función para dibujar la cuadrícula
def dibujar_cuadricula():
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            pygame.draw.rect(pantalla, GRIS, (columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA), 1)

# O(1) generar_posicion_zapote ------ 


def generar_posicion_zapote(disponibles):
    (zapote_x, zapote_y) = random.choice(disponibles)
    return zapote_x, zapote_y, random.randint(0, 10)
    # while True:
    #     posibles_posiciones = [(x, y) for x in range(COLUMNAS) for y in range(FILAS)]
    #     posibles_posiciones = [pos for pos in posibles_posiciones if pos not in serpiente]
    #     if posibles_posiciones:
    #         return random.choice(posibles_posiciones)

    
# Función principal del juego
def juego():
    # O(N)
    disponibles = [(x, y) for x in range(COLUMNAS) for y in range(FILAS)]
    cabeza_x = COLUMNAS // 2
    cabeza_y = FILAS // 2
    serpiente = [(cabeza_x, cabeza_y), (cabeza_x , cabeza_y+1), (cabeza_x , cabeza_y+2)]
    direccion = None
    zapote_timido = 0
    zapote_maduro = 0
    # Posición Inicial zapote
    zapote_x, zapote_y = 9,3
    pygame.draw.rect(pantalla, NEGRO, (zapote_x * TAMANO_CELDA, zapote_y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
    

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
                if keys[pygame.K_a]:
                    direccion = 'izquierda'
                elif keys[pygame.K_d]:
                    direccion = 'derecha'
                elif keys[pygame.K_w]:
                    direccion = 'arriba'
               
                
        else:
            # Movimiento de la serpiente después de comenzar el juego
            if keys[pygame.K_a] and direccion != 'derecha':
                direccion = 'izquierda'
            elif keys[pygame.K_d] and direccion != 'izquierda':
                direccion = 'derecha'
            elif keys[pygame.K_w] and direccion != 'abajo':
                direccion = 'arriba'
            elif keys[pygame.K_s] and direccion != 'arriba':
                direccion = 'abajo'
            

            if direccion == 'izquierda':
                cabeza_x -= 1
            elif direccion == 'derecha':
                cabeza_x += 1
            elif direccion == 'arriba':
                cabeza_y -= 1
            elif direccion == 'abajo':
                cabeza_y += 1
            
            if any(keys):
                zapote_timido += 1

            # Verificar colisión con los bordes
            if cabeza_x < 0 or cabeza_x >= COLUMNAS or cabeza_y < 0 or cabeza_y >= FILAS:
                perdido = True            

            # Verificar colisión con la serpiente
            if (cabeza_x, cabeza_y) in serpiente[1:]:
                perdido = True

            serpiente.insert(0, (cabeza_x, cabeza_y))
            #print("-"*50, "\n\n\n",disponibles)
            if perdido != True:
                disponibles.remove(serpiente[0])

            # Comer elle zapote
            if cabeza_x == zapote_x and cabeza_y == zapote_y  :
                zapote_x, zapote_y, zapote_maduro = generar_posicion_zapote(disponibles)
            
                if zapote_timido == zapote_maduro:
                    zapote_timido = 0
                    pygame.draw.rect(pantalla, NEGRO, (zapote_x * TAMANO_CELDA, zapote_y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
                
            else:
                disponibles.append(serpiente.pop())


        # Dibujar fondo
        pantalla.fill(BLANCO)

        # Dibujar serpiente
        for segmento in serpiente:
            if segmento == serpiente[0]:
                pygame.draw.ellipse(pantalla, GRIS, (segmento[0] * TAMANO_CELDA, segmento[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
            else:
                pygame.draw.ellipse(pantalla, GRIS_CLARO, (segmento[0] * TAMANO_CELDA, segmento[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
        # Dibujar zapote
        # pygame.draw.rect(pantalla, NEGRO, (zapote_x * TAMANO_CELDA, zapote_y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))

        # Dibujar cuadrícula
        dibujar_cuadricula()

        # Mostrar puntuación en la pantalla
        fuente = pygame.font.Font(None, 36)
        texto_puntuacion = fuente.render(f"Puntuación: {zapote_timido}", True, NEGRO)
        pantalla.blit(texto_puntuacion, (10, 395))

        pygame.display.update()
        pygame.time.delay(100)

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
