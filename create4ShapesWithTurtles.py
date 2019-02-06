import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(10)
#square
for i in range(4):
    tess.forward(50)
    tess.left(90)

tess.penup()
tess.right(180)
tess.forward(50)
tess.pendown()
#triangle
for i in range(3):
        tess.forward(50)
        tess.right(120)

tess.penup()
tess.left(90)
tess.forward(50)
tess.pendown()
#octagon
for i in range(8):
        tess.forward(50)
        tess.right(45)
tess.penup()
tess.left(90)
tess.forward(100)
tess.pendown()
#hexagon
for i in range(6):
        tess.forward(80)
        tess.right(60)
        
wn.exitonclick()
