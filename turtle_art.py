import turtle

turtle.shape("turtle")
turtle.speed(1)

# turtle square box shape
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

# turtle shape
for i in range(6):
    turtle.forward(200)
    turtle.left(60)

# turtle tryangle (pyramid)
for i in range(3):
    turtle.right(60)
    turtle.forward(300)
    turtle.right(60)

# dashed line
for i in range(10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

for side_length in range(50, 100, 10):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)


turtle.exitonclick()
