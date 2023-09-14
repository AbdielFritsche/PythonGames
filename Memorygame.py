"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path
ntaps = 0
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
uncovered_tiles = 0 #definir variable

def draw_square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
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
            draw_square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+25, y) #Agregamos a la posicion x +25
        color('black')
        write(tiles[mark],align = "center",font=('Arial', 30, 'normal'))
        #Agregamos el align = "center" a la funcion write para alinear en el centro los numeros
        
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
