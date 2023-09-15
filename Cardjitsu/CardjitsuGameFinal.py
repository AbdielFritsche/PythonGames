import turtle
import random
import time
from carta import Carta
import comandos

# Variables globales con nombres cortos pero representativos
j_mano = []  # Mano del jugador
c_mano = []  # Mano de la computadora
manos = [j_mano, c_mano]
j_vic = 0  # Victorias del jugador
c_vic = 0  # Victorias de la computadora
emp = 0  # Empates
enc = 0  # Encuentros
elems = ["Fuego", "Agua", "Nieve"]  # Elementos del juego
niveles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Niveles de poder de las cartas

# Función para mostrar al ganador
def mostrar_ganador(jug):
    """
    Muestra al ganador de la partida o si terminó en empate.

    Parametros:
    jug (str): El nombre del jugador que ganó o "Empate" si fue un empate.
    """
    global enc
    turtle.clearscreen()
    turtle.bgcolor("green")
    turtle.ht()
    turtle.penup()
    turtle.goto(0, 0)
    if jug == "Jugador" or jug == "Computadora":
        if jug == "Jugador":
            turtle.write(f"Ganaste la partida después de {enc} encuentros", align="center", font=("Arial", 50, "normal"))
        else:
            turtle.write(f"La computadora te ha derrotado, buena suerte para la próxima", align="center", font=("Arial", 50, "normal"))
    else:
        turtle.write(f"La partida terminó en un empate", align="center", font=("Arial", 50, "normal"))
    turtle.penup()
    time.sleep(5)
    turtle.update()

# Función para anunciar al ganador
def anunciar_ganador(jug):
    """
    Anuncia al ganador de un encuentro o si terminó en empate.

    Parametros:
    jug (str): El nombre del jugador que ganó o "Empate" si fue un empate.
    """
    global enc
    turtle.clearscreen()
    turtle.bgcolor("green")
    turtle.ht()
    turtle.penup()
    turtle.goto(0, 0)
    if jug == "Jugador" or jug == "Computadora":
        turtle.write(f"{jug} gana el encuentro número {enc}", align="center", font=("Arial", 50, "normal"))
    else:
        turtle.write(f"El encuentro número {enc} terminó en un empate", align="center", font=("Arial", 50, "normal"))
    turtle.penup()
    time.sleep(5)
    turtle.clearscreen()
    turtle.bgcolor("green")
    turtle.update()

# Función para escribir las reglas
def escribir_reglas():
    """
    Escribe las reglas del juego en la pantalla de inicio.
    """
    turtle.clearscreen()
    turtle.bgcolor("green")
    turtle.ht()
    turtle.penup()
    turtle.goto(0, 400)
    turtle.write(f"Bienvenido al juego de cartas. Las reglas son las siguientes:", align="center", font=("Arial", 30, "normal"))
    time.sleep(1)
    turtle.goto(0, 300)
    turtle.write(f"Agua vence al fuego", align="center", font=("Arial", 30, "normal"))
    time.sleep(1)
    turtle.penup()
    turtle.goto(0, 200)
    turtle.write(f"Fuego vence a la nieve", align="center", font=("Arial", 30, "normal"))
    time.sleep(1)
    turtle.penup()
    turtle.goto(0, 100)
    turtle.write(f"Nieve vence al agua", align="center", font=("Arial", 30, "normal"))
    time.sleep(1)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write(f"En caso de empate se decide por la carta de mayor nivel", align="center", font=("Arial", 30, "normal"))
    turtle.penup()
    time.sleep(1)
    turtle.goto(0, -100)
    turtle.write(f"Preparando partida . . .", align="center", font=("Arial", 30, "normal"))
    turtle.penup()
    time.sleep(5)
    turtle.clearscreen()
    turtle.bgcolor("green")
    turtle.update()

# Función para mostrar el marcador
def mostrar_marcador():
    """
    Muestra el marcador con la cantidad de encuentros, victorias y empates.
    """
    global j_vic
    global c_vic
    global emp
    global enc
    turtle.ht()
    turtle.penup()
    turtle.goto(0, 400)
    turtle.write(f"Encuentros: {enc}", align="center", font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(850, 200)
    turtle.write(f"Victorias jugador: {j_vic}", align="right", font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(850, 150)
    turtle.write(f"Victorias computadora: {c_vic}", align="right", font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(850, 100)
    turtle.write(f"Empates: {emp}", align="right", font=("Arial", 20, "normal"))
    turtle.penup()

# Función para verificar al ganador de una partida
def verificar_ganador(j, c):
    """
    Verifica el ganador de una partida de acuerdo a las reglas del juego.

    Parametros:
    j (Carta): La carta seleccionada por el jugador.
    c (Carta): La carta seleccionada por la computadora.

    Returns:
    str: El resultado de la partida ("Jugador gana", "Computadora gana" o "Empate").
    """
    global j_vic
    global c_vic
    global emp
    turtle.onscreenclick(None)
    if j.elemento == "Fuego" and c.elemento == "Nieve" or j.elemento == "Nieve" and c.elemento == "Agua" or j.elemento == "Agua" and c.elemento == "Fuego":
        j_vic += 1
        anunciar_ganador("Jugador")
        return "Jugador gana"
    elif j.elemento == c.elemento:
        if j.nivel_de_poder > c.nivel_de_poder:
            j_vic += 1
            anunciar_ganador("Jugador")
            return "Jugador gana"
        elif j.nivel_de_poder < c.nivel_de_poder:
            c_vic += 1
            anunciar_ganador("Computadora")
            return "Computadora gana"
        else:
            emp += 1
            anunciar_ganador("Empate")
            return "Empate"
    else:
        c_vic += 1
        anunciar_ganador("Computadora")
        return "Computadora gana"

# Función para manejar el clic en una carta
def clic_en_carta(x, y):
    """
    Maneja el evento de clic en una carta del juego.

    Parametros:
    x (int): La posición x del clic.
    y (int): La posición y del clic.
    """
    turtle.onscreenclick(None)
    global carta_jugador, carta_computadora, enc
    enc += 1
    for carta in j_mano:
        if x >= carta.x - 50 and x <= carta.x + 50 and y >= carta.y - 75 and y <= carta.y + 75:
            carta_jugador = carta
            comandos.dibujar_carta(carta_jugador.elemento, carta_jugador.nivel_de_poder, 150, 0, "tablero")
            print(f"Carta seleccionada por el jugador: {carta.elemento}, Nivel: {carta.nivel_de_poder}")
            carta_computadora = random.choice(c_mano)
            comandos.dibujar_carta(carta_computadora.elemento, carta_computadora.nivel_de_poder, -150, 0, "tablero")
            print(f"Carta seleccionada por la computadora: {carta_computadora.elemento}, Nivel: {carta_computadora.nivel_de_poder}")
            time.sleep(2)
            resultado = verificar_ganador(carta_jugador, carta_computadora)
            print(resultado)
            time.sleep(2)
            j_mano.remove(carta_jugador)
            c_mano.remove(carta_computadora)
            mostrar_marcador()
            comandos.crear_tablero()
            comandos.dibujar_mano(j_mano, "jugador", -300)
            comandos.dibujar_mano(c_mano, "computadora", 300)
            turtle.update()

# Iniciar el juego
def iniciar_juego():
    """
    Inicia el juego, muestra las reglas, el marcador y las manos iniciales.
    """
    turtle.setup(width=1.0, height=1.0)
    escribir_reglas()
    comandos.crear_tablero()
    mostrar_marcador()
    comandos.dibujar_mano(j_mano, "jugador", -300)
    comandos.dibujar_mano(c_mano, "computadora", 300)
    turtle.update()

# Crear las manos iniciales
def crear_manos_iniciales(elementos, niveles_de_poder):
    """
    Crea las manos iniciales de cartas para el jugador y la computadora.

    Parametros:
    elementos (list): Lista de elementos disponibles.
    niveles_de_poder (list): Lista de niveles de poder disponibles.
    """
    cartas_elementales = []
    for i in range(30):
        carta = Carta(elementos[random.randint(0, 2)], niveles_de_poder[random.randint(0, 9)])
        cartas_elementales.append(carta)
    for i in range(7):
        for jugador in manos:
            carta_elegida = cartas_elementales[random.randint(0, len(cartas_elementales) - 1)]
            jugador.append(carta_elegida)
            cartas_elementales.remove(carta_elegida)

# Función principal del juego
def jugar_partida():
    """
    Función principal que controla el flujo del juego.
    """
    global elems
    global niveles
    crear_manos_iniciales(elems, niveles)
    iniciar_juego()
    while len(j_mano) >= 0 and len(c_mano) >= 0:
        if j_vic == c_vic + 3:
            mostrar_ganador("Jugador")
            print("El encuentro lo gana el jugador")
            turtle.bye()
            break
        elif c_vic == j_vic + 3:
            mostrar_ganador("Computadora")
            print("El encuentro lo gana la computadora")
            turtle.bye()
            break
        else:
            if enc == 7 and c_vic > j_vic:
                mostrar_ganador("Computadora")
                print("El encuentro lo gana la computadora")
                turtle.bye()
                break
            elif enc == 7 and c_vic < j_vic:
                mostrar_ganador("Jugador")
                print("El encuentro lo gana el jugador")
                turtle.bye()
                break
            elif enc == 7 and c_vic == j_vic:
                mostrar_ganador("Empate")
                print("El encuentro termina en un empate")
                turtle.bye()
                break
        turtle.onscreenclick(clic_en_carta)
        turtle.update()

# Iniciar el juego
jugar_partida()
