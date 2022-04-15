# Getting started
import turtle

wn = turtle.Screen()
wn.title("My Pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
p_a = turtle.Turtle()
p_a.speed(0)
p_a.shape("square")
p_a.color("red")
p_a.shapesize(stretch_wid=5, stretch_len=1)
p_a.penup()
p_a.goto(-350,0)

# Paddle B
p_b = turtle.Turtle()
p_b.speed(-5)
p_b.shape("square")
p_b.color("blue")
p_b.shapesize(stretch_wid=5, stretch_len=1)
p_b.penup()
p_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

#function
def p_a_up():
    y = p_a.ycor()
    y+=20
    p_a.sety(y)

def p_a_down():
    y = p_a.ycor()
    y-=20
    p_a.sety(y)

def p_b_up():
    y = p_b.ycor()
    y+=20
    p_b.sety(y)

def p_b_down():
    y = p_b.ycor()
    y-=20
    p_b.sety(y)
    
# keyboard binding

wn.listen()
wn.onkeypress(p_a_up, "w")
wn.onkeypress(p_a_down, "s")
wn.onkeypress(p_b_up, "Up")
wn.onkeypress(p_b_down, "Down")
    
# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    # paddle and ball collisions

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < p_b.ycor() + 40 and ball.ycor() > p_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < p_a.ycor() + 40 and ball.ycor() > p_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1