print("Welcome to turtle racing! Please enter the following informations: ")

def get_number_of_racers():
    turtle_number = 0
    while True:
        turtle_number = input("How many turtles would you like to race[2-10]?: ")
        if turtle_number.isdigit():
            turtle_number = int(turtle_number)
        else:
            print("Imput is not numeric...Try Again")
            continue

        if 2 <= turtle_number <= 10:
            return turtle_number
        else:
            print("number not in range 2-10. Try again")


racers = get_number_of_racers()
