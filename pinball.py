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

#flipper1
f1 = t.Turtle()
f1.shape("triangle")
f1.shapesize(1, 4, 1)
f1.penup()
f1.goto(-60, -240)
f1.tilt(345)

#flipper2
f2 = t.Turtle()
f2.shape("triangle")
f2.shapesize(1, 4, 1)
f2.penup()
f2.goto(60, -240)
f2.tilt(195)

#flipper walls
fwall1 = t.Turtle()
fwall1.shape("square")
fwall1.shapesize(1, 4, 1)
fwall1.penup()
fwall1.goto(-120 ,-200)
fwall1.tilt(315)

fwall2 = t.Turtle()
fwall2.shape("square")
fwall2.shapesize(1, 4, 1)
fwall2.penup()
fwall2.goto(120, -200)



t.done()

