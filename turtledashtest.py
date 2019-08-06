import turtle

turtle.speed(1)
turtle.shape("turtle")

for i in range(30):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick()
