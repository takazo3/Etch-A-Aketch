import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.fd(10)


def backwards():
    tim.bk(10)


def counter_clockwise():
    tim.lt(10)


def clockwise():
    tim.rt(10)


def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
