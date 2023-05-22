import turtle, time, random


WIDTH, HEIGHT = 600, 600
x_left_corner = -300
y_left_corner = 300
distance = int(WIDTH // 3)


def init_window():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Tic Tac Toe game!")
    screen.bgcolor("black")
    return screen


# shape siatka
def init_mesh(x, y, distance):
    hero = init_object()
    for a in [1, 2]:
        hero.penup()
        hero.goto(x + a * distance, y)
        hero.pendown()
        hero.goto(x + a * distance, -y)

        hero.penup()
        hero.goto(x, y - a * distance)
        hero.pendown()
        hero.goto(- x, y - a * distance)


def init_object():
    hero = turtle.Turtle()
    hero.color("white")
    hero.pensize(7)
    hero.speed(0)
    hero.hideturtle()
    return hero


window = init_window()
init_mesh(x_left_corner, y_left_corner, distance)
time.sleep(5)

table = [[None, None, None],
        [None, None, None],
        [None, None, None]]

#adresowanie [wiersz],[kolumna]

turn = random.choice(['x','o'])


def click(x, y):
        pass

window.onclick(click)


window.listen()
window.mainloop()