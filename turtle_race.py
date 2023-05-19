import turtle, time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "cyan", "orange", "yellow", "black", "purple", "pink", "brown"]

print("Welcome to turtle racing! Please enter the following informations: ")

def get_number_of_racers():
    turtle_number = 0
    while True:
        turtle_number = input("How many turtles would you like to race[2-10]?: ")
        if turtle_number.isdigit():
            turtle_number = int(turtle_number)
        else:
            print("Input is not numeric...Try Again")
            continue

        if 2 <= turtle_number <= 10:
            return turtle_number
        else:
            print("number not in range 2-10. Try again")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 15)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Championships!")


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(winner + " turtle is a new champion")
time.sleep(5)