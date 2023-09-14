from turtle import *
from random import randrange, randint, choice  # Importa randint y choice de random
from freegames import square, vector

# Lista de colores para la serpiente y la comida (excluyendo el rojo para la comida y la serpiente)
snake_colors = ['brown', 'black', 'yellow','violet', 'blue']
food_colors = ['blue', 'green', 'purple', 'orange', 'pink']

# Asigna colores aleatorios iniciales para la serpiente y la comida al inicio del programa 
snake_color = choice(snake_colors)
food_color = choice(food_colors)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    global snake_color, food_color  # Declarar  el color de la serpiente y de la comida como globales

    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

        # Asigna nuevos colores aleatorios para la serpiente y la comida
        snake_color = choice(snake_colors)
        food_color = choice(food_colors)
    else:
        snake.pop(0)
    
    # Genera un movimiento aleatorio para la comida como se pide en el primer punto de la actividad 
    random_move = vector(randint(-1, 1) * 10, randint(-1, 1) * 10)
    food.move(random_move)
    # Hacer que cada vez que la comida tiene un movimiento aleatorio esta misma no se salga de la ventana 
    food.x = max(min(food.x, 190), -200)
    food.y = max(min(food.y, 190), -200)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
