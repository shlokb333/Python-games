# My snake game

# Making the sanke
import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("My Snake game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

t = turtle.Turtle()
t.shape("square")
t.speed(0)
t.penup()
t.color("white")
t.goto(0,0)
t.direction = "stop"




# Snake's food
f = turtle.Turtle()
colors = random.choice(["red", "blue", "green"])
shapes = random.choice(["square", "triangle", "circle"])
f.speed(0)
f.shape(shapes)
f.color(colors)
f.penup()
f.goto(0,100)

segments=[]
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,25)
pen.write("Score: 0  Highscore :0", align="center", font=("arial",24,"bold"))


# functions

def go_up():
    if t.direction !="down":
        t.direction="up"
def go_down():
    if t.direction !="up":
        t.direction="down"
def go_left():
    if t.direction !="right":
        t.direction="left"
def go_right():        
    if t.direction !="left":
        t.direction="right"    
def move():
    if t.direction== "up":
        y=t.ycor()
        t.sety(y+20)
    if t.direction== "down":
        y=t.ycor()
        t.sety(y-20)
    if t.direction== "left":
        x=t.xcor()
        t.set(x+20)
    if t.direction== "right":
        x=t.xcor()
        t.sety(x-20)

'''def t_up():
    y = t.ycor()
    y+=20
    t.sety(y)
def t_down():
    y = t.ycor()
    y-=20
    t.sety(y)
def t_left():
    x = t.xcor()
    x-=20
    t.setx(x)
def t_right():
    x = t.xcor()
    x+=20
    t.setx(x)'''
    
# keyboard binding

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
    
# Main game loop
while True:
    wn.update()
    if t.xcor()>290 or t.xcor()<-290 or t.ycor()>290 or t.ycor()<-290:
        time.sleep(1)
        t.goto(0,0)
        t.direction = "stop"
        colors = random.choice(["red", "blue", "green"])
        shapes = random.choice(["square", "triangle", "circle"])
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score : {} Highscore : {}".format(score,high_score),align="center",font=("arial",24,"bold"))
    if t.distance(food)<20:
        x=random.randint(-270,270)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment .speed(0)
        new_segment .shape("square")
        new_segment .color("grey")
        new_segment .penup()
        new_segment.append(new_segment)
        delay -=0.001
        score +=10
        if score > high_score:
            high_score=score
        pen.clear()
        pen.write("Score :{} Highscore :{}".format(score,high_score,align="center",font=("arial",24,"bold"))
    for index in range(len(segment)-1,0,-1) :
        x=segments[index-1.xcor()]
        y=segments[index-1.ycor()]
        segments[index].goto(x,y)
    if len(segemets)>0:
        x = t.xcor()
        y = t.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(t)<20:
            time.sleep(1)
            t.goto(0,0)
            t.direction = "stop"
            colors = random.choice(["red", "blue", "green"])
            shapes = random.choice(["square", "triangle", "circle"])
            
        
wn.mainloop()
turtle.done()