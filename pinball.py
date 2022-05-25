import turtle as t

window = t.Screen()
window.bgcolor("white")

#ball
ball = t.Turtle()
ball.shape("circle")
ball.penup()
ball.goto(235, -160)

#walls
wall = t.Turtle()
wall.hideturtle()
wall.penup()
wall.goto(250, -290)
wall.width(3)
wall.pendown()
wall.goto(250, 290)
wall.goto(-250, 290)
wall.goto(-250, -290)
wall.goto(250, -290)
wall.penup()
wall.goto(220, -290)
wall.pendown()
wall.goto(220, 200)
wall.penup()
#circle
wall.goto(250, 200)
wall.left(90)
wall.pendown()
wall.circle(90, 90)
wall.penup()
wall.goto(-160, 290)
wall.pendown()
wall.circle(90, 90)
#triangle
wall.penup()
wall.goto(-250, -200)
wall.pendown()
wall.goto(-160, -290)
wall.penup()
wall.goto(220, -200)
wall.pendown()
wall.goto(130, -290)

#flippers
f1 = t.Turtle()
f1.shape("triangle")
f1.shapesize(1, 4, 1)
f1.penup()


t.done()
