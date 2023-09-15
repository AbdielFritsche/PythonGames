import turtle
import random

ventana = turtle.Screen()
ventana.bgcolor("green")

mi_tortuga = turtle.Turtle()
mi_tortuga.speed(1000)

def rectangle(x, y):
    """
    Dibuja un rectángulo con lados de longitud 'x' y 'y'.

    Args:
        x (int): Longitud del lado horizontal.
        y (int): Longitud del lado vertical.
    """
    for i in range(4):
        if i % 2 == 0:
            mi_tortuga.forward(x)
            mi_tortuga.right(90)
        else:
            mi_tortuga.forward(y)
            mi_tortuga.right(90)

def mostrar_carta(elemento, nivel_de_poder, x, y):
    """
    Muestra una carta en la posición (x, y) con el elemento y nivel de poder especificados.

    Args:
        elemento (str): El elemento de la carta (p. ej., "Fuego", "Agua", "Nieve").
        nivel_de_poder (int): El nivel de poder de la carta.
        x (int): La coordenada x de la posición de la carta.
        y (int): La coordenada y de la posición de la carta.
    """
    mi_tortuga.penup()
    mi_tortuga.goto(x, y)
    mi_tortuga.pendown()
    
    if elemento == "Fuego":
        mi_tortuga.color("Red")
    elif elemento == "Nieve":
        mi_tortuga.color("Cyan")
    else:
        mi_tortuga.color("Blue")
        
    mi_tortuga.write(elemento, align="center", font=("Arial", 15, "normal"))
    
    mi_tortuga.penup()
    mi_tortuga.goto(x, y - 100)
    mi_tortuga.pendown()
    mi_tortuga.color("black")
    mi_tortuga.write(f"Nivel: {nivel_de_poder}", align="center", font=("Arial", 12, "normal"))

def dibujar_carta(elemento, nivel_de_poder, x, y, jugador):
    """
    Dibuja una carta en la posición (x, y) con el elemento y nivel de poder especificados.

    Args:
        elemento (str): El elemento de la carta (p. ej., "Fuego", "Agua", "Nieve").
        nivel_de_poder (int): El nivel de poder de la carta.
        x (int): La coordenada x de la posición de la carta.
        y (int): La coordenada y de la posición de la carta.
        jugador (str): El nombre del jugador o "tablero".
    """
    mi_tortuga.pensize(10)
    mi_tortuga.ht()
    mi_tortuga.penup()
    mi_tortuga.home()
    mi_tortuga.penup()
    mi_tortuga.goto(x - 50, y + 75)
    mi_tortuga.pendown()
    
    if jugador == "jugador" or jugador == "tablero":
        if elemento == "Fuego":
            mi_tortuga.fillcolor("orange") 
        elif elemento == "Agua":
            mi_tortuga.fillcolor("cyan")
        else:
            mi_tortuga.fillcolor("white")
        mi_tortuga.begin_fill()
    else:
        mi_tortuga.fillcolor("black")
        mi_tortuga.begin_fill()

    rectangle(100, 150)
    mi_tortuga.end_fill()
    
    if jugador == "jugador":
        mostrar_carta(elemento, nivel_de_poder, x, y)
    elif jugador == "tablero":
        mostrar_carta(elemento, nivel_de_poder, x, y)

def dibujar_mano(mano, jugador, posYi):
    """
    Dibuja una mano de cartas para el jugador en la posición vertical especificada.

    Args:
        mano (list): La lista de cartas que componen la mano.
        jugador (str): El nombre del jugador ("jugador" o "computadora").
        posYi (int): La coordenada y inicial para la posición de las cartas.
    """
    espaciado_x = 150
    x = -len(mano) * espaciado_x / 2.25
    y_jugador = posYi

    for carta in mano:
        mi_tortuga.penup()
        mi_tortuga.home()
        carta.x = x
        carta.y = y_jugador
        dibujar_carta(carta.elemento, carta.nivel_de_poder, x, y_jugador, jugador)
        x += espaciado_x

def crear_tablero():
    """
    Dibuja el tablero de juego en la ventana de Turtle.
    """
    mi_tortuga.ht()
    mi_tortuga.penup()
    mi_tortuga.goto(-500, -150)
    mi_tortuga.pendown()
    mi_tortuga.color("brown")
    mi_tortuga.begin_fill()

    for i in range(2):
        mi_tortuga.forward(1000)
        mi_tortuga.left(90)
        mi_tortuga.forward(350)
        mi_tortuga.left(90)

    mi_tortuga.end_fill()
    
    mi_tortuga.penup()
    mi_tortuga.goto(0, -150)
    mi_tortuga.pendown()
    mi_tortuga.pensize(10)
    mi_tortuga.color("black")
    mi_tortuga.forward(0)
    mi_tortuga.left(90)
    mi_tortuga.forward(350)
    mi_tortuga.pensize(1)
    mi_tortuga.penup()

if __name__ == "__main__":
    pass


    
