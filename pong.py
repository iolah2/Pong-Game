# Simple @Pong Game for beginners in Python3
# by Norbert-Dev
#----------------------------------------->

# Private Note
# Sound is optional and can be imported
# To import just download any sound u like and rename the [SOUND] tag
# Also dont forget to remove the hastag in front if the relevant os

# IRÁNYÍTÁS::
#
# Left Player / Bal oldali Játékos - Player A 
# Up / Fel - W
# Down / Le - S
#
# Right Player / Jobb oldali Játékos - Player B 
# Up / Fel - Up arrow / Felfelé nyíl
# Down / Le - Down Arrow / Lefelé nyíl
#------------------------------------------>

import turtle
# import os             # This is for MAC
# import winsound       # This is for WIN

# Basic Screen details
wn = turtle.Screen()
wn.title("Pong by Norbet-Dev")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pontozás

pont_a = 0
pont_b = 0

#-------------------------------------->
### Pálya rajz
#-------------------------------------->

# Középkör
keret = turtle.Turtle()
keret.color("white")
keret.shape("circle")
keret.penup()
keret.setposition(-50, -50)
keret.pendown()
keret.pensize(2)
keret.ht() # vagy keret.hideturtle() elrejti a turtlet

for i in range(4):
    keret.forward(100)
    keret.left(90)

# Közép vonal
midline = turtle.Turtle()
midline.color("white")
midline.shape("square")
midline.penup()
midline.setposition(1, 0)
midline.pendown()
midline.pensize(2)
midline.ht()

# Közép vonal rajza

midline.left(90)
midline.forward(250)
midline.left(90)
midline.forward(1)
midline.left(90)
midline.forward(500)
midline.left(90)
midline.forward(1)
midline.left(90)
midline.forward(500)

#-------------------------------------->
### Játékosok és labda
#-------------------------------------->

# Ütő A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Ütő B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Labda
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("lightgray")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pontok - Default state
toll = turtle.Turtle()
toll.speed(0)
toll.color("white")
toll.penup()
toll.hideturtle()
toll.goto(0, 260)
toll.write("0   :   0", align="center", font=("Courier", 24, "normal"))

# Irányítás - Controlls
"""
toll_1 = turtle.Turtle()
toll_1.speed(0)
toll_1.color("gray")
toll_1.penup()
toll_1.hideturtle()
toll_1.goto(0, 0)
toll_1.write("w - fel   :   Up arrow - fel", align="center", font=("Courier", 24, "normal"))
"""

# Funkciók
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Funkció hívása

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Game LOOP
while True:
    wn.update()

    # Labda mozgás
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Határok ellenőrzése
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("afplay [SOUND]&") #This is for MAC
        #os.system("aplay [SOUND]&") #This is for Linux
        #winsound.PlaySound("[SOUND]", winsound.SND_ASYNC) #This is for WIN

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #os.system("afplay [SOUND]&") #This is for MAC
        #os.system("aplay [SOUND]&") #This is for Linux
        #winsound.PlaySound("[SOUND]", winsound.SND_ASYNC) #This is for WIN

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = 1 / 10
        ball.dx *= -1
        pont_a += 1
        toll.clear()
        toll.write("{}   :   {}".format(pont_a, pont_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 1 / 10
        ball.dx *= -1
        pont_b += 1
        toll.clear()
        toll.write("{}   :   {}".format(pont_a, pont_b), align="center", font=("Courier", 24, "normal"))

    if paddle_a.ycor() > 250: 
        paddle_a.goto(-350, 250)
    
    if paddle_a.ycor() < -250:
        paddle_a.goto(-350, -250)

    if paddle_b.ycor() > 250: 
        paddle_b.goto(350, 250)
    
    if paddle_b.ycor() < -250:
        paddle_b.goto(350, -250)
        
    # Ütő és Labda ütközés

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        ball.dx -= 0.15
        #os.system("afplay [SOUND]&") #This is for MAC
        #os.system("aplay [SOUND]&") #This is for Linux
        #winsound.PlaySound("[SOUND]", winsound.SND_ASYNC) #This is for WIN

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx += 0.15
        #os.system("afplay [SOUND]&") #This is for MAC
        #os.system("aplay [SOUND]&") #This is for Linux
        #winsound.PlaySound("[SOUND]", winsound.SND_ASYNC) #This is for WIN
