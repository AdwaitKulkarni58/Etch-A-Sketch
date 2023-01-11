from turtle import Turtle, Screen
my_turtle = Turtle()


def move_forwards():
    my_turtle.forward(5)
    
def move_backwards():
    my_turtle.left()
    my_turtle.left()
    my_turtle.backward(5)


my_screen = Screen()
my_screen.onkeypress(move_forwards, "Right")
my_screen.onkeypress(move_backwards, "Left")
my_screen.listen()
my_screen.exitonclick()
