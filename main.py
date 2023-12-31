#setup
import turtle
zain = turtle.Turtle()
wn = turtle.Screen()
wn.title("Beach")
wn.bgcolor("blue")
wn.setup(width = 800, height = 800)
zain.color("black")
turtle.hideturtle()
turtle.speed(0)

#cordinate clicking tool 
def buttonclick(x,y):
    print("You clicked at this cordinate({0},{1})".format(x,y))
turtle.onscreenclick(buttonclick, 1)

#sand
zain.penup()
zain.goto(-395, -380)
zain.pendown()
zain.color("pale goldenrod")
zain.begin_fill()
for i in range(1):
    zain.left(25)
    zain.forward(900)
    zain.right(115)
    zain.forward(1000)
zain.end_fill()

#sky
zain.penup()
zain.goto(-400,217)
zain.pendown()
zain.color("deep sky blue")
zain.begin_fill()
for i in range(2):
    zain.forward(-1600)
    zain.right(90)
    zain.forward(-800)
    zain.right(90)
zain.end_fill()

#sun
zain.penup()
zain.goto(235,302)
zain.pendown()
zain.color("yellow")
zain.begin_fill()
zain.circle(75)
zain.end_fill()

#clouds (Credit trinket for almost all these directions)
zain.penup()
zain.goto(-7,245)
zain.pendown()
zain.color("azure")
zain.begin_fill()
zain.left(90)
zain.forward(150)
zain.left(90)
zain.forward(20)
for i in range (1, 15):
  zain.left(10)
  zain.forward(10)
zain.left(220)
for i in range (1,18):
  zain.left(10)
  zain.forward(12)
zain.left(200)
for i in range (1,18):
  zain.left(10)
  zain.forward(15)
zain.forward(18)
zain.left(90)
zain.forward(260)
zain.end_fill()

#fishes (credit to quickprogammingtips for giving directions for the traignle)
zain.penup()
zain.goto(-301,4)
zain.pendown()
zain.color("gold")
zain.begin_fill()
zain.right(50)
zain.forward(100)
zain.left(120)
zain.forward(100)
zain.left(120)
zain.forward(100)
zain.end_fill()

zain.penup()
zain.goto(-183,94)
zain.pendown()
zain.color("gold")
zain.begin_fill()
zain.circle(45)
zain.end_fill()

zain.penup()
zain.goto(-158,64)
zain.pendown()
zain.color("black")
zain.begin_fill()
zain.circle(10)
zain.end_fill()

#shark (credit pythondex for almost all directions)
zain.penup()
zain.goto(-60,-65)
zain.pendown()
zain.color("dim gray")
zain.begin_fill()
zain.right(150)
zain.left(45)
zain.forward(100)
zain.right(135)
zain.forward(130)
zain.right(130)
zain.forward(90)
zain.left(90)
zain.right(90)
zain.circle(200,90)
zain.left(90)
zain.circle(200,90)
zain.end_fill()

zain.penup()
zain.goto(-223,-229)
zain.pendown()
zain.color("navy")
zain.begin_fill()
zain.circle(10)
zain.end_fill()

#boat (Credit Geek Tutorials for the bottom of the boat and credit quickprogammingtips for almost all directions for the right triganle)
zain.penup()
zain.goto(-15,74)
zain.pendown()
zain.color("sienna")
zain.begin_fill()
zain.left(-450)
zain.right(45)
zain.forward(100)
zain.left(45)
zain.forward(250)
zain.left(45)
zain.forward(100)
zain.end_fill()

zain.penup()
zain.goto(174,73)
zain.pendown()
zain.color("black")
zain.begin_fill()
for i in range(1):
    zain.left(45)
    zain.forward(125)
zain.end_fill()

zain.penup()
zain.goto(175,196)
zain.pendown()
zain.color("white")
zain.begin_fill()
zain.right(540)
zain.forward(100)
zain.left(90)
zain.forward(100)
zain.left(135)
zain.forward(142)
zain.end_fill()

zain.penup()
zain.goto(73,96)
zain.pendown()
zain.color("white")
zain.begin_fill()
zain.right(495)
zain.forward(100)
zain.left(90)
zain.forward(100)
zain.left(135)
zain.forward(142)
zain.end_fill()

#starfish (on left side)
zain.penup()
zain.goto(-129, -278)
zain.pendown()
zain.color("chocolate")
zain.begin_fill()
for i in range(5):
    zain.fd (100)
    zain.left(144)
zain.end_fill()

#beach umbrella

zain.penup()
zain.goto(2,-363)
zain.pendown()
zain.color("navy")
zain.begin_fill()
for i in range(1):
    zain.left(45)
    zain.forward(-100)
zain.end_fill()

zain.penup()
zain.goto(50,-264)
zain.pendown()
zain.color("alice blue")
zain.begin_fill()
zain.left(200)
zain.circle(50,140)
zain.end_fill()

#mat
zain.penup()
zain.goto(67,-374)
zain.pendown()
zain.color("medium turquoise")
zain.begin_fill()
zain.left(200)
zain.forward(100)
zain.left(90)
zain.forward(50)
zain.left(90)
zain.forward(100)
zain.left(90)
zain.end_fill()

#beach ball
zain.penup()
zain.goto(191,-245)
zain.pendown()
zain.color("midnight blue")
zain.begin_fill()
zain.circle(20)
zain.end_fill()

#star fishes (right)
zain.penup()
zain.goto(290, -117)
zain.pendown()
zain.color("chocolate")
zain.begin_fill()
for i in range(5):
    zain.fd (100)
    zain.left(144)
zain.end_fill()

#stick figure in the boat
zain.penup()
zain.goto(317,135)
zain.pendown()
zain.color("navajo white")
zain.begin_fill()
zain.circle(35)
zain.end_fill()

zain.penup()
zain.goto(317,135)
zain.pendown()
zain.color("navajo white")
zain.begin_fill()
for i in range (1):
    zain.left(90)
    zain.forward(-60)
zain.end_fill()

zain.penup()
zain.goto(319,104)
zain.pendown()
zain.color("navajo white")
zain.begin_fill()
for i in range (1):
    zain.right(110)
    zain.forward(50)
zain.end_fill()

zain.penup()
zain.goto(316,104)
zain.pendown()
zain.color("navajo white")
zain.begin_fill()
for i in range (1):
    zain.right(170)
    zain.forward(60)
zain.end_fill()

zain.penup()
zain.goto(301,176)
zain.pendown()
zain.color("peru")
zain.begin_fill()
zain.circle(5)
zain.end_fill()

zain.penup()
zain.goto(329,176)
zain.pendown()
zain.color("peru")
zain.begin_fill()
zain.circle(5)
zain.end_fill()

#stick figure laying on the mat
zain.penup()
zain.goto(45,-280)
zain.pendown()
zain.color("blanched almond")
zain.begin_fill()
zain.circle(20)
zain.end_fill()

zain.penup()
zain.goto(41,-320)
zain.pendown()
zain.color("blanched almond")
zain.begin_fill()
for i in range(1):
    zain.right(80)
    zain.forward(-30)
zain.end_fill()

zain.penup()
zain.goto(40,-336)
zain.pendown()
zain.color("blanched almond")
zain.begin_fill()
for i in range(1):
    zain.right(80)
    zain.forward(-20)
zain.end_fill()

zain.penup()
zain.goto(42,-336)
zain.pendown()
zain.color("blanched almond")
zain.begin_fill()
for i in range(1):
    zain.left(150)
    zain.forward(-20)
zain.end_fill()

zain.penup()
zain.goto(41,-351)
zain.pendown()
zain.color("blanched almond")
zain.begin_fill()
for i in range(1):
    zain.right(100)
    zain.forward(-20)
zain.end_fill()

zain.penup()
zain.goto(41,-351)
zain.pendown()
zain.color("blanched almond")
zain.begin_fill()
for i in range(1):
    zain.left(75)
    zain.forward(-20)
zain.end_fill()

zain.penup()
zain.goto(36,-296)
zain.pendown()
zain.color("black")
zain.begin_fill()
zain.circle(3)
zain.end_fill()

zain.penup()
zain.goto(51,-296)
zain.pendown()
zain.color("black")
zain.begin_fill()
zain.circle(3)
zain.end_fill()

#stick figure playing with the beach ball

zain.penup()
zain.goto(292,-152)
zain.pendown()
zain.color("tan")
zain.begin_fill()
zain.circle(30)
zain.end_fill()

zain.penup()
zain.goto(271,-204)
zain.pendown()
zain.color("tan")
zain.begin_fill()
for i in range(1):
    zain.right(45)
    zain.forward(-47)
zain.end_fill()

zain.penup()
zain.goto(271,-228)
zain.pendown()
zain.color("tan")
zain.begin_fill()
for i in range(1):
    zain.right(100)
    zain.forward(-45)
zain.end_fill()

zain.penup()
zain.goto(271,-228)
zain.pendown()
zain.color("tan")
zain.begin_fill()
for i in range(1):
    zain.left(200)
    zain.forward(-45)
zain.end_fill()

zain.penup()
zain.goto(271,-252)
zain.pendown()
zain.color("tan")
zain.begin_fill()
for i in range(1):
    zain.left(250)
    zain.forward(-50)
zain.end_fill()

zain.penup()
zain.goto(271,-252)
zain.pendown()
zain.color("tan")
zain.begin_fill()
for i in range(1):
    zain.right(-45)
    zain.forward(-50)
zain.end_fill()

zain.penup()
zain.goto(267,-165)
zain.pendown()
zain.color("saddle brown")
zain.begin_fill()
zain.circle(6)
zain.end_fill()

zain.penup()
zain.goto(287,-165)
zain.pendown()
zain.color("saddle brown")
zain.begin_fill()
zain.circle(6)
zain.end_fill()

#Initials at bottom right in darker brown

def zain_initial():
    zain.color("saddle brown")
    zain.penup()
    zain.goto(285,-390)
    style = ('Times', 84, 'bold')
    zain.write('ZS', font=style)
    zain.hideturtle()

zain_initial()
turtle.done()