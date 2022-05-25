import turtle as t

window = t.Screen()
window.bgcolor("white")

ball = t.Turtle()
ball.shape("circle")
ball.penup()
ball.goto(150,0)
ball.done()

wall = t.Turtle()
wall.penup()
wall.goto(170, -20)
wall.done()
