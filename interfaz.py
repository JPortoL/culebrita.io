import turtle


grid_size = 13
screen_size = 650
factor_mv = screen_size / grid_size

ventana = turtle.Screen()
ventana.title("Juego Snake")
ventana.bgcolor("black")
ventana.setup(width=screen_size, height=screen_size)

#elementos de tortuga
def creacion_elementos(forma,color):
    elemento = turtle.Turtle()
    elemento.speed()
    elemento.penup()
    elemento.shape(forma)
    elemento.color(color)
    elemento.goto(0,0)
    return elemento

def main():
    cabeza = creacion_elementos("square","white")
    cabeza.direccion = 'stop'
    comida = creacion_elementos('circle','red')
    comida.goto(0,90)
    #Funciones para las direcciones
    def arriba():
        cabeza.direccion = 'Up'
        movimiento_snake(cabeza)
        print("arriba")
    def abajo():
        cabeza.direccion = 'Down'
        movimiento_snake(cabeza)
    def izquierda():
        cabeza.direccion = 'Left'
        movimiento_snake(cabeza)
    def derecha():
        cabeza.direccion = 'Right'
        movimiento_snake(cabeza)

    #teclado
    ventana.listen()
    ventana.onkeypress(arriba,'Up')
    ventana.onkeypress(abajo,'Down')
    ventana.onkeypress(izquierda,'Left')
    ventana.onkeypress(derecha,'Right')

    ventana.mainloop()

#Funcion para movimiento
def movimiento_snake(cabeza):
    #movimiento vertical
    if cabeza.direccion == 'Up':
        y = cabeza.ycor()
        cabeza.sety(y+factor_mv)
    if cabeza.direccion == 'Down':
        y = cabeza.ycor()
        cabeza.sety(y-factor_mv)
    #movimiento horizontal
    if cabeza.direccion == 'Left':
        x = cabeza.xcor()
        cabeza.setx(x-factor_mv)
    if cabeza.direccion == 'Right':
        x = cabeza.xcor()
        cabeza.setx(x+factor_mv)

main()