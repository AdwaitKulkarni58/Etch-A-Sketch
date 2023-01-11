from turtle import Turtle, Screen
my_turtle = Turtle()


def move_forwards():
    my_turtle.forward(5)


def move_backwards():
    my_turtle.backward(5)


def rotate_left():
    my_turtle.left(5)


def rotate_right():
    my_turtle.right(5)


my_screen = Screen()

my_screen.onkeypress(move_forwards, "w")
my_screen.onkeypress(move_backwards, "s")
my_screen.onkeypress(rotate_left, "a")
my_screen.onkeypress(rotate_right, "d")

my_screen.listen()
my_screen.exitonclick()
