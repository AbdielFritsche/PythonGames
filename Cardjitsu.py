from carta import Carta
import comandos
import turtle
import random
import time

    
num_jugadores = 2  # Puedes ajustar el número de jugadores
mano_jugador = list()
mano_computadora = list()
manos = [mano_jugador , mano_computadora]
vic_jug = 0
vic_bot = 0
empates = 0 

# Crear una lista de elementos y niveles de poder
elementos = ["Fuego", "Agua", "Nieve"]
niveles_de_poder = [1,2,3,4,5,6,7,8,9,10]

#Función para verificar el ganador
def verificar_ganador(c_jug, c_bot):
    global vic_jug 
    global vic_bot 
    global empates 
    turtle.onscreenclick(None)
    # Comparar las cartas según las reglas del juego
    if c_jug.elemento == "Fuego" and c_bot.elemento == "Nieve" or c_jug.elemento == "Nieve" and c_bot.elemento == "Agua" or c_jug.elemento == "Agua" and c_bot.elemento == "Fuego":
        vic_jug +=1
        return "Jugador gana"
    elif c_jug.elemento == c_bot.elemento:
        if c_jug.nivel_de_poder > c_bot.nivel_de_poder:
            vic_jug +=1
            return "Jugador gana"
        elif c_jug.nivel_de_poder < c_bot.nivel_de_poder:
           vic_bot +=1
           return "Computadora gana"
        else:
            empates +=1
            return "Empate"
    else:
        vic_bot +=1
        return "Computadora gana"
        
# Función para manejar el clic en una carta
def clic_en_carta(x, y):
    turtle.onscreenclick(None)
    global carta_seleccionada_jugador, carta_seleccionada_computadora

    # Verificar si el clic ocurrió en una carta del jugador
    for carta in mano_jugador:
        if x >= carta.x - 50 and x <= carta.x + 50 and y >= carta.y - 75 and y <= carta.y + 75:
            carta_seleccionada_jugador = carta  # Carta seleccionada por el jugador
            comandos.dibujar_carta(carta_seleccionada_jugador.elemento,carta_seleccionada_jugador.nivel_de_poder,150,0,"tablero")
            print(f"Carta seleccionada por el jugador: {carta.elemento}, Nivel: {carta.nivel_de_poder}")

            # Seleccionar una carta aleatoria para la computadora
            carta_seleccionada_computadora = random.choice(mano_computadora)
            comandos.dibujar_carta(carta_seleccionada_computadora.elemento,carta_seleccionada_computadora.nivel_de_poder,-150,0,"tablero")
            print(f"Carta seleccionada por la computadora: {carta_seleccionada_computadora.elemento}, Nivel: {carta_seleccionada_computadora.nivel_de_poder}")
            
            # Verificar el ganador
            resultado = verificar_ganador(carta_seleccionada_jugador, carta_seleccionada_computadora)
            print(resultado)
            time.sleep(5)
            mano_jugador.remove(carta_seleccionada_jugador)
            mano_computadora.remove(carta_seleccionada_computadora)
            
            turtle.clearscreen()
            turtle.bgcolor("green")
            comandos.crear_tablero()
            comandos.dibujar_mano(mano_jugador, "jugador",-300)
            comandos.dibujar_mano(mano_computadora, "computadora",300)
            turtle.update()
            #comandos.actualizar_recuentos()


# Crear una lista de cartas elementales
cartas_elementales = []
for i in range(30):
    carta = Carta(elementos[random.randint(0,2)],niveles_de_poder[random.randint(0,9)])
    cartas_elementales.append(carta)
    
for i in range(7):
    for jugador in manos:
        carta_elegida = cartas_elementales[random.randint(0,len(cartas_elementales)-1)]
        jugador.append(carta_elegida)
        cartas_elementales.remove(carta_elegida)

turtle.setup(width=1.0, height=1.0)
comandos.crear_tablero()
comandos.dibujar_mano(mano_jugador, "jugador",-300)
comandos.dibujar_mano(mano_computadora, "computadora",300)
turtle.update()

while len(mano_jugador) >= 0 and len(mano_computadora) >=0:
    if len(mano_jugador) == 0 and len(mano_computadora) == 0:
        if vic_jug > vic_bot:
            print("El encuentro lo gana el jugador")
            exit(0)
        elif vic_jug < vic_bot:
            print("El encuentro lo gana el jugador")
            exit(0)
        else:
            print("El encuentro termina en un empate")
            exit(0)
    else:
        turtle.onscreenclick(clic_en_carta)
        turtle.update()

    