import turtle

screen = turtle.Screen()
screen.setup(500, 500)

turtle.pensize(2)
turtle.pencolor()
turtle.shape("turtle")
# turtle.hideturtle()
turtle.speed(1)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)

screen.exitonclick()