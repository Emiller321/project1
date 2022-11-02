import turtle
import time
import random

delay = 0.1

#Score 
score = 0
high_score = 0

#Set up the screen 
wn = turtle.Screen()
wn.title("Jetpack by Eric Miller")
wn.bgcolor("light blue")
wn.setup(width = 600, height = 600)
wn.tracer(0) #turns off the screen updates


#Airplane
ap = turtle.Turtle()
ap.speed(0)
ap.shape("triangle")
ap.color("white")
ap.penup()
ap.goto(0,0)
ap.direction = "stop"

#Creating Multiple ENemys
maxEnemys = 6
enemys = []

for count in range(maxEnemys):
    enemys.append(turtle.Turtle())
    enemys[count].speed(3)
    enemys[count].shape("circle")
    enemys[count].color("black")
    enemys[count].penup()
    enemys[count].goto(0,100)
    enemys[count].direction = "left"

#Canon 
canon = turtle.Turtle()
canon.shape("circle")
canon.color("yellow")
canon.penup()
canon.speed(0)
canon.setheading(90)
canon.shapesize(0.5,0.5)
canon.hideturtle()

canonspeed = 20
bulletstate = "ready"

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align = "center", font = ("Courier", 24, "normal") )

speed = 10

#Functions
def go_left():
    ap.left(30)

def go_right():
    ap.right(30)


def fire_canon():
    global bulletstate

    x = ap.xcor()
    y = ap.ycor() + 10
    canon.setposition(x, y)
    canon.showturtle()
    

#Keyboard Binings
turtle.listen()
turtle.onkeypress(go_left, "Left")
turtle.onkeypress(go_right, "Right")
turtle.onkeypress(fire_canon, "space")


# Main Game Loop
while True:
    ap.forward(speed)
    wn.update()

    #Check for collision with border
    if ap.xcor() > 290 or ap.xcor() < -290 or ap.ycor() > 290 or ap.ycor() < -290:
        time.sleep(1)
        ap.goto(0,0)
        ap.direction = "stop"

    if enemys[count].xcor() > 290 or enemys[count].xcor() < -290 or enemys[count].ycor() > 290 or enemys[count].ycor() < -290:
        time.sleep(1)
        enemys[count].goto(0,0)
        enemys[count].direction = "stop"

    # Moving the Canon
    y = canon.ycor()
    y += canonspeed
    canon.sety(y)

    if ap.distance(enemys[count]) < 20:
        turtle.quit()

    if canon.distance(enemys[count]) < 20:
        #move Bullet to random spot
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        enemys[count].goto(x, y)

        #Increase the Score
        score += 10

        if score > high_score:
            high_score = score
    
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

    time.sleep(delay)