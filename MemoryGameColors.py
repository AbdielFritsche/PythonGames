from random import *
from turtle import *

from freegames import path
ntaps = 0
car = path('car.gif')
colors = ['#FF5733', '#33FF57', '#5733FF', '#FF33E8', 
          '#33E8FF', '#E833FF', '#FFEC33', '#33FFEC',
          '#FFA07A', '#20B2AA', '#00CED1', '#8A2BE2',
          '#FF1493', '#FFD700', '#98FB98', '#800080',
          '#ADFF2F', '#FF4500', '#32CD32', '#FF00FF',
          '#00FF7F', '#FF69B4', '#7B68EE', '#FFFF00',
          '#DA70D6', '#00FFFF', '#8B008B', '#FFFFE0',
          '#FA8072', '#1E90FF', '#FFC0CB', '#7FFF00']

#Colores en hexadecimales

tiles = colors * 2
state = {'mark': None}
hide = [True] * 64   
uncovered_tiles = 0

#funcion para asociarle colores al grid en vez de numeros
def draw_square(x, y, tile_color):
    """Draw colored square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black',tile_color)
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global ntaps , uncovered_tiles
    spot = index(x, y)
    mark = state['mark']
    ntaps += 1
    taps()

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        uncovered_tiles+=2 #Agregar en 2 el numero de tiles descubiertas
        
    if uncovered_tiles == len(tiles):
        print("Has descubierto todos los tiles") #si se encuentran todas dar este mensaje en consola
        
def draw():
    """Draw image and tiles."""
    goto(0, 0)
    shape(car)
    stamp()
    
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            draw_square(x, y, 'white') #por default el color del grid debe de ser blanco

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y)
        color('black')
        draw_square(x, y, tiles[mark]) # al hacer click en un tile el tile debe de mostrar el color de esa posicion

    update()
    ontimer(draw, 100)

#crear una funcion que ayude a registrar el numero de taps despues de cada click
def taps():
     global ntaps 
     clear()
     up()
     goto(0, 300) #Agregamos a la posicion x +25
     color('black')
     write(f"Numero de clicks: {ntaps}", align="right", font=("Arial", 20, "normal"))  
     update()

shuffle(tiles)
setup(680, 680, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
