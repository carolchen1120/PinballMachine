import turtle as t

window = t.Screen()
window.bgcolor("white")

ball = t.Turtle()
ball.shape("circle")
ball.penup()
ball.goto(150, -160)
ball.done()

wall = t.Turtle()
wall.penup()
wall.goto(190, -240)
wall.pendown()
wall.goto(190, 160)
wall.goto(-190, 160)

wall.done()
