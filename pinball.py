import turtle as t
from turtle import *
import math
import random

window = t.Screen()
window.title("Pinball Machine")
window.bgcolor("white")
window.angle = 10

t.tracer(2, 0)

#ball
ball = t.Turtle()
ball.shape("circle")
ball.penup()
ball.goto(235, -190)
ball.vel = 1
ball.score = 0
ball.yvel = 1
ball.dx = random.randrange(-3, 3)
ball.dy = 1
ball.free = False
ball.secs = 0

#write score
writer = t.Turtle()
writer.speed(0)
writer.color("blue")
writer.penup()
writer.hideturtle()
writer.goto(0, 300)
writer.write(f'Score = {ball.score}', align = "center", font=("Courier", 24, "normal"))

#launcher
block = t.Turtle()
block.shape("square")
block.shapesize(1, 6, 1)
block.penup()
block.goto(235, -260)
block.tilt(90)
block.color('lightgreen')
block.press = -1

#walls
wall = t.Turtle()
wall.hideturtle()
wall.penup()
wall.goto(250, -320)
wall.width(3)
wall.pendown()
wall.goto(250, 290)
wall.goto(-250, 290)
wall.goto(-250, -320)
wall.goto(250, -320)
wall.penup()
wall.goto(220, -320)
wall.pendown()
wall.goto(220, 200)
wall.penup()

#circle
wall.goto(250, 200)
wall.left(90)
wall.pendown()
wall.circle(90, 90)

#triangle
wall.penup()
wall.goto(-250, -230)
wall.pendown()
wall.goto(-160, -320)
wall.penup()
wall.goto(220, -230)
wall.pendown()
wall.goto(130, -320)

#flippers
f1 = t.Turtle()
f1.flip = False
f1.shape("triangle")
f1.shapesize(1, 4, 1)
f1.penup()
f1.goto(-75, -270)
f1.tilt(345)

f2 = t.Turtle()
f2.flip = False
f2.shape("triangle")
f2.shapesize(1, 4, 1)
f2.penup()
f2.goto(45, -270)
f2.tilt(195)

#pivots
piv1 = t.Turtle()
piv1.shape("circle")
piv1.penup()
piv1.goto(-100, -263)
piv1.shapesize(.8, .8, .8)

piv2 = t.Turtle()
piv2.shape("circle")
piv2.penup()
piv2.goto(70, -263)
piv2.shapesize(.8, .8, .8)

#flipper walls
fwall1 = t.Turtle()
fwall1.shape("square")
fwall1.shapesize(.9, 5, 1)
fwall1.penup()
fwall1.goto(-145 ,-220)
fwall1.tilt(315)

fwall2 = t.Turtle()
fwall2.shape("square")
fwall2.shapesize(.9, 5, 1)
fwall2.penup()
fwall2.goto(115, -220)
fwall2.tilt(45)

fwall3 = t.Turtle()
fwall3.shape("square")
fwall3.shapesize(.9, 5, 1)
fwall3.penup()
fwall3.goto(-182.5, -130)
fwall3.tilt(90)

fwall4 = t.Turtle()
fwall4.shape("square")
fwall4.shapesize(.9, 5, 1)
fwall4.penup()
fwall4.goto(152.5, -130)
fwall4.tilt(90)

#obstacles-rectangles
owall1 = t.Turtle()
owall1.shape("square")
owall1.shapesize(.8, 4, 1)
owall1.penup()
owall1.goto(-90, 170)
owall1.tilt(45)

owall2 = t.Turtle()
owall2.shape("square")
owall2.shapesize(.8, 2, 1)
owall2.penup()
owall2.goto(-95, 131)
owall2.tilt(135)

owall5 = t.Turtle()
owall5.shape("square")
owall5.shapesize(.2, 2, 1)
owall5.color("red")
owall5.penup()
owall5.goto(27, 143)
owall5.tilt(45)

owall6 = t.Turtle()
owall6.shape("square")
owall6.shapesize(.2, 2, 1)
owall6.color("red")
owall6.penup()
owall6.goto(93, 143)
owall6.tilt(135)

owall3 = t.Turtle()
owall3.shape("square")
owall3.shapesize(.8, 2.5, 1)
owall3.penup()
owall3.goto(20, 150)
owall3.tilt(45)

owall4 = t.Turtle()
owall4.shape("square")
owall4.shapesize(.8, 2.5, 1)
owall4.penup()
owall4.goto(100, 150)
owall4.tilt(135)

owall7 = t.Turtle()
owall7.shape("square")
owall7.shapesize(.15, 2.5, 1)
owall7.color("red")
owall7.penup()
owall7.goto(-247, 125)
owall7.tilt(90)

owall8 = t.Turtle()
owall8.shape("square")
owall8.shapesize(.8, 2.5, 1)
owall8.penup()
owall8.goto(196.5, 46.5)
owall8.tilt(45)

owall9 = t.Turtle()
owall9.shape("square")
owall9.shapesize(.8, 2, 1)
owall9.penup()
owall9.goto(-45, 65)
owall9.tilt(135)

owall10 = t.Turtle()
owall10.shape("square")
owall10.shapesize(.8, 3, 1)
owall10.penup()
owall10.goto(-70, 60)
owall10.tilt(45)

owall11 = t.Turtle()
owall11.shape("square")
owall11.shapesize(.15, 2, 1)
owall11.color("red")
owall11.penup()
owall11.goto(216, -5)
owall11.tilt(90)

owall12 = t.Turtle()
owall12.shape("square")
owall12.shapesize(.8, 2.25, 1)
owall12.penup()
owall12.goto(97, -10)
owall12.tilt(45)

owall13 = t.Turtle()
owall13.shape("square")
owall13.shapesize(.8, 2.25, 1)
owall13.penup()
owall13.goto(120, -10)
owall13.tilt(135)

owall14 = t.Turtle()
owall14.shape("square")
owall14.shapesize(.8, 2, 1)
owall14.penup()
owall14.goto(-231, 171)
owall14.tilt(135)

#obstacle-circles
ocircle1 = t.Turtle()
ocircle1.shape("circle")
ocircle1.shapesize(1.25, 1.25, 1.25)
ocircle1.penup()
ocircle1.goto(170, 100)

ocircle2 = t.Turtle()
ocircle2.shape("circle")
ocircle2.shapesize(1.25, 1.25, 1.25)
ocircle2.penup()
ocircle2.goto(-170, 90)

ocircle3 = t.Turtle()
ocircle3.shape("circle")
ocircle3.shapesize(3, 3, 3)
ocircle3.color("red")
ocircle3.penup()
ocircle3.goto(60, 70)

ocircle4 = t.Turtle()
ocircle4.shape("circle")
ocircle4.shapesize(2.75, 2.75, 2.75)
ocircle4.color("red")
ocircle4.penup()
ocircle4.goto(-215, 20)

#obstacle-triangles
otriangle1 = t.Turtle()
otriangle1.shape("triangle")
otriangle1.shapesize(.95, .55, 1)
otriangle1.penup()
otriangle1.goto(215, 70)
otriangle1.tilt(180)

otriangle2 = t.Turtle()
otriangle2.shape("triangle")
otriangle2.shapesize(.95, .55, 1)
otriangle2.penup()
otriangle2.goto(-245, 191)

#obstacle-diamond
odiamond1 = t.Turtle()
odiamond1.shape("square")
odiamond1.shapesize(.8, .8, 1)
odiamond1.penup()
odiamond1.goto(-110, 0)
odiamond1.tilt(45)

odiamond2 = t.Turtle()
odiamond2.shape("square")
odiamond2.shapesize(.8, .8, .8)
odiamond2.penup()
odiamond2.goto(-150, 0)
odiamond2.tilt(45)


t.tracer(1, 1)


#flipper function
def flip_left():
    if not f1.flip:
        f1.flip = True
        f1.left(45)
        f1.right(45)
        f1.flip = False



def flip_right():
    if not f2.flip:
        f2.flip = True
        f2.right(45)
        f2.left(45)
        f2.flip = False


def pull_down():
    block.press += 1
    if block.press == 0:
        block.color('yellow')
        ball.vel = 4
    elif block.press == 1:
        block.color('orange')
        ball.vel = 6
    elif block.press == 2:
        block.color('red')
        ball.vel = 9


def launch():
    while True:
        ball.right(90)
        if ball.xcor() == 235 and ball.ycor() < 210:
            for i in range(-190, 220, ball.vel):
                ball.sety(i)
        elif ball.xcor() == 235 and ball.ycor() > 210:
            move_circle()
            ball.free = True
            ball.dy = -ball.vel

            
def move_circle() :
    ball.right(90)
    ball.circle(60, 90)
    ball.goto(0, ball.ycor())

    
def free_fall():
    g = -5 * math.cos(window.angle * math.pi / 180)
    x = ball.dx
    ball.dy += g * 0.5     # change in y vel = accel * time interval
    y = ball.ycor()
    y += ball.dy * 0.5          # change in y posn = vel + time interval 
    ball.goto(x, y)


def black_collision() :
    cors_a = ball.xcor() + ball.ycor() # sum of coordinates of ball's center
    cors_s = ball.ycor() - ball.xcor() # difference of coordinates of ball's center
    # circle obstacles
    if abs(ball.xcor() - ocircle1.xcor()) <= 22.5 and abs(ball.ycor() - ocircle1.ycor()) <= 22.5 :
        ball.dy *= -1
        ball.dx *= -1
    elif abs(ball.xcor() - ocircle2.xcor()) <= 22.5 and abs(ball.ycor() - ocircle2.ycor()) <= 22.5 :
        ball.dy *= -1
        ball.dx *= -1
    elif abs(ball.xcor() - ocircle3.xcor()) <= 40 and abs(ball.ycor() - ocircle3.ycor()) <= 40 :
        ball.dy *= -1
        ball.dx *= -1
    elif abs(ball.xcor() - ocircle4.xcor()) <= 37.5 and abs(ball.ycor() - ocircle4.ycor()) <= 37.5 :
        ball.dy *= -1
        ball.dx *= -1
    # rectangle obstacles
    # owall3 and owall5
    elif ((cors_s <= 130+2*math.sqrt(8)) and (cors_s >= 130-2*math.sqrt(8)) and
                            (cors_a >= 170-2*math.sqrt(25)) and (cors_a <= 170+2*math.sqrt(25))) :
        ball.dy *= -1
        ball.dx *= -1
        # need to include red spring action (owall5)
    # owall4 and owall6
    elif ((cors_s <= 50+2*math.sqrt(25)) and (cors_s >= 50-2*math.sqrt(25)) and
                            (cors_a >= 250-2*math.sqrt(8)) and (cors_a <= 250+2*math.sqrt(8))) :
        ball.dy *= -1
        ball.dx *= -1
        # need to include red spring action (owall4)
    # need to include red spring for owall7
    # owall8
    elif ((cors_s <= 243+2*math.sqrt(8)) and (cors_s >= 243-2*math.sqrt(8)) and
                            (cors_a >= -150-2*math.sqrt(25)) and (cors_a <= -150+2*math.sqrt(25))) :
        ball.dy *= -1
        ball.dx *= -1
    # owall9
    elif ((cors_s <= 110+2*math.sqrt(20)) and (cors_s >= 110-2*math.sqrt(20)) and
                            (cors_a >= 20-2*math.sqrt(8)) and (cors_a <= 20+2*math.sqrt(8))) :
        ball.dy *= -1
        ball.dx *= -1
    # owall10
    elif ((cors_s <= 130+2*math.sqrt(8)) and (cors_s >= 130-2*math.sqrt(8)) and
                            (cors_a >= -10-2*math.sqrt(30)) and (cors_a <= -10+2*math.sqrt(30))) :
        ball.dy *= -1
        ball.dx *= -1
    # need to include red spring for owall11
    # owall12
    elif ((cors_s <= -117+2*math.sqrt(8)) and (cors_s >= -117-2*math.sqrt(8)) and
                            (cors_a >= 87-2*math.sqrt(22.5)) and (cors_a <= 87+2*math.sqrt(22.5))) :
        ball.dy *= -1
        ball.dx *= -1
    # owall13
    elif ((cors_s <= -130+2*math.sqrt(22.5)) and (cors_s >= -130-2*math.sqrt(22.5)) and
                            (cors_a >= 110-2*math.sqrt(8)) and (cors_a <= 110+2*math.sqrt(8))) :
        ball.dy *= -1
        ball.dx *= -1
    # owall14
    elif ((cors_s <= 400+2*math.sqrt(20)) and (cors_s >= 400-2*math.sqrt(20)) and
                            (cors_a >= 60-2*math.sqrt(8)) and (cors_a <= 60+2*math.sqrt(8))) :
        ball.dy *= -1
        ball.dx *= -1
    else :
        g = -1 * math.cos(window.angle * math.pi / 180)
        x = ball.dx * ball.secs
        ball.dy += g * 0.5     # change in y vel = accel * time interval
        y = ball.ycor()
        y += ball.dy * 0.5       # change in y posn = vel + time interval 
        ball.goto(x, y)
        ball.secs += 1


# SPECIAL OBSTACLES
# owall1 = t.Turtle()
# owall1.shape("square")
# owall1.shapesize(.8, 4, 1)
# owall1.penup()
# owall1.goto(-90, 170)
# owall1.tilt(45)

# owall2 = t.Turtle()
# owall2.shape("square")
# owall2.shapesize(.8, 2, 1)
# owall2.penup()
# owall2.goto(-95, 131)
# owall2.tilt(135)



t.listen()

t.onkey(flip_left, "Left")
t.onkey(flip_right, "Right")
t.onkey(pull_down, 'space')
t.onkey(launch, 'l')


def tick() :
    if ball.xcor() > -250 and ball.xcor() < 250 and ball.ycor() > -320 and ball.ycor() < 292 and ball.free == True :
        # free_fall()
        black_collision()
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)
        writer.clear()
        writer.write(f'Score = {ball.score}', align = "center", font=("Courier", 24, "normal"))

    if ball.ycor() < -290 :
        t.clearscreen()
        new_write = t.Turtle()
        new_write.speed(0)
        new_write.color("blue")
        new_write.penup()
        new_write.hideturtle()
        new_write.write(f'Your score was {ball.score}. Thank you for playing!', align = "center", font=("Courier", 24, "normal"))
        t.delay(100)
        return True

    window.update()
    window.ontimer(tick, 60)
    
tick()
window.mainloop()
        

# # Gravity code
# # setup variables for time, x step, gravity, initial velocity 
# t=0
# tstep = 0.25    # seconds   
# delx = 2        # uniform motion in x axis 
# g = -1          # fixed accel (downwards) 
# yvel = 20       # initial vel in y 
# y=0             # y position 

# # draw a cliff that the ball can be thrown from 
# penup()
# goto(-100,0)
# pendown()
# color("green")
# forward(150)
# right(90)
# forward(100)
# penup()
# goto(0,0)

# pendown()
# color("blue")

# print("run the simulation for 50 seconds ")
# # main loop -- uniform motion in x and acceleration in y axis 
# while (t<50):
#     t=t+tstep
#     x=t*delx
#     yvel = yvel + g * tstep     # change in y vel = accel * time interval
#     y=y + yvel * tstep          # change in y posn = vel + time interval 
    
#     goto(x,y)
#     dot(2, "blue")              # draw dot at current position 

# print("final y position is " + str(y) + " m")



    
# def rounded_rectangle(turtle, short, long, radius):
# #     diameter = radius * 2
# #
# #     heading = turtle.heading()
# #     turtle.setheading(270)
# #
# #     isdown = turtle.isdown()
# #     if isdown:
# #         turtle.penup()
# #
# #     turtle.goto(turtle.xcor() - long/2, turtle.ycor() - short/2 + radius)
# #
# #     turtle.pendown()
# #
# #     for _ in range(2):
# #         turtle.circle(radius, 90)
# #         turtle.forward(long - diameter)
# #         turtle.circle(radius, 90)
# #         turtle.forward(short - diameter)
# #
# #     turtle.penup()  # restore turtle state, position and heading
# #     turtle.goto(turtle.xcor() + long/2, turtle.ycor() + short/2 - radius)
# #     if isdown:
# #         turtle.pendown()
# #     turtle.setheading(heading)
# #
# # exam = t.Turtle()
# # rounded_rectangle(exam, 60, 90, 10)

# t.done()
