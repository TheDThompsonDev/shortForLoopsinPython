import turtle

wn = turtle.Screen()

jess = turtle.Turtle()

sides = input("How many sides?")
sides = int(sides)
length = input("What is the length of the side?")
length = int(length)
turt_color = input("what color would you like?")
bgc = input("what color would you like the polygon to be?")

jess.color(turt_color)
angles = int(360/sides)
jess.fillcolor(bgc)
jess.begin_fill()

for i in range(sides):
    jess.forward(length)
    jess.right(angles)
    
jess.end_fill()
    
    
