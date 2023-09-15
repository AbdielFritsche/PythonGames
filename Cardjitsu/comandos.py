import turtle
import random

# Crear una ventana de Turtle para dibujar las cartas
ventana = turtle.Screen()
ventana.bgcolor("green")

# Crear una instancia de la clase Turtle para dibujar
mi_tortuga = turtle.Turtle()
mi_tortuga.speed(1000)  # Configurar la velocidad de dibujo más rápida

def rectangle(x,y):
    for i in range(4):
        if  i % 2 == 0:
            mi_tortuga.forward(x)
            mi_tortuga.right(90)
        else:
            mi_tortuga.forward(y)
            mi_tortuga.right(90)

def mostrar_carta(elemento, nivel_de_poder,x, y):
    # Mostrar el elemento en el centro
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
    
    # Mostrar el nivel de poder en la esquina inferior derecha
    mi_tortuga.penup()
    mi_tortuga.goto(x, y - 100)
    mi_tortuga.pendown()
    mi_tortuga.color("black")
    mi_tortuga.write(f"Nivel: {nivel_de_poder}", align="center", font=("Arial", 12, "normal"))
        
def dibujar_carta(elemento, nivel_de_poder, x, y,jugador):
    mi_tortuga.pensize(10)
    mi_tortuga.ht()
    mi_tortuga.penup()
    mi_tortuga.home()
    # Dibujar el contorno de la carta en la posición (x, y)
    mi_tortuga.penup()
    mi_tortuga.goto(x - 50, y + 75)
    mi_tortuga.pendown()
    mi_tortuga.color("black")
    if jugador == "jugador" or jugador == "tablero" :
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

    rectangle(100,150)
    mi_tortuga.end_fill()

    
    # Mostrar el elemento en el centro
    if jugador == "jugador":
        mostrar_carta(elemento, nivel_de_poder,x, y)
    elif jugador =="tablero":
        mostrar_carta(elemento, nivel_de_poder,x, y)
    else:
        pass
# Función para dibujar una mano de cartas
def dibujar_mano(mano, jugador,posYi):
    espaciado_x = 150  # Espaciado horizontal entre cartas
    x =-len(mano) * espaciado_x / 2.25
    y_jugador = posYi

    for carta in mano:
        mi_tortuga.penup()
        mi_tortuga.home()
        carta.x = x  # Establece la coordenada x de la carta
        carta.y = y_jugador  # Establece la coordenada y de la carta
        dibujar_carta(carta.elemento, carta.nivel_de_poder, x, y_jugador,jugador)
        x += espaciado_x

#Funcion para dibujar el tablero
def crear_tablero():
    mi_tortuga.ht()
    # Dibuja el contorno del tablero
    mi_tortuga.penup()
    mi_tortuga.goto(-500, -150)  # Ajusta las coordenadas para el tablero
    mi_tortuga.pendown()
    mi_tortuga.color("brown")
    mi_tortuga.begin_fill()
    for i in range(2):
        mi_tortuga.forward(1000)  # Ancho del tablero
        mi_tortuga.left(90)
        mi_tortuga.forward(350)  # Alto del tablero
        mi_tortuga.left(90)
    mi_tortuga.end_fill()

    # Dibuja la división en el medio del tablero
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
    