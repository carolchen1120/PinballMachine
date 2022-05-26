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
f1.goto(-75, -240)
f1.tilt(345)

f2 = t.Turtle()
f2.shape("triangle")
f2.shapesize(1, 4, 1)
f2.penup()
f2.goto(45, -240)
f2.tilt(195)

#pivots
piv1 = t.Turtle()
piv1.shape("circle")
piv1.penup()
piv1.goto(-100, -233)
piv1.shapesize(.8, .8, .8)

piv2 = t.Turtle()
piv2.shape("circle")
piv2.penup()
piv2.goto(70, -233)
piv2.shapesize(.8, .8, .8)

#flipper walls
fwall1 = t.Turtle()
fwall1.shape("square")
fwall1.shapesize(.9, 5, 1)
fwall1.penup()
fwall1.goto(-145 ,-190)
fwall1.tilt(315)

fwall2 = t.Turtle()
fwall2.shape("square")
fwall2.shapesize(.9, 5, 1)
fwall2.penup()
fwall2.goto(115, -190)
fwall2.tilt(45)

fwall3 = t.Turtle()
fwall3.shape("square")
fwall3.shapesize(.9, 5, 1)
fwall3.penup()
fwall3.goto(-182.5, -100)
fwall3.tilt(90)

fwall4 = t.Turtle()
fwall4.shape("square")
fwall4.shapesize(.9, 5, 1)
fwall4.penup()
fwall4.goto(152.5, -100)
fwall4.tilt(90)

#bottom triangles
btri1 = t.Turtle()
btri1.shape("triangle")
btri1.shapesize(7, 2, 1)
btri1.penup()
btri1.goto(-125, -125)
btri1.tilt(205)

btri2 = t.Turtle()
btri2.shape("triangle")
btri2.shapesize(7, 2, 1)
btri2.penup()
btri2.goto(95, -125)
btri2.tilt(335)

#objects
owall1 = t.Turtle()
owall1.shape("square")
owall1.shapesize(.9, 4, 1)
owall1.penup()
owall1.goto(-70 ,160)
owall1.tilt(315)


t.done()

