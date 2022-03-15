from turtle import *
from random import *
background = getscreen()
background.bgcolor("black")
shape("turtle")
colormode(255)
pensize(5)
speed(0)

def randomly_draw():
    size = getscreen().screensize()
    xmax = size[0]
    ymax = size[1]
    randomX = randrange(-xmax,xmax)
    randomY = randrange(-ymax,ymax)
    penup()
    setposition((randomX, randomY))
    pendown()
    pencolor(randrange(0,100),randrange(0,100),randrange(150,255))
    fillcolor(randrange(0,255),randrange(0,255),randrange(0,255))
    ###Calls the function you defined
    myshape()

###Change this function so it draws a shape of your choosing
def myshape():
    begin_fill()
    circle(10)
    end_fill()

    
numShapes = int(numinput("Enter a number", "How many shapes would you like?", 10, 0))

for i in range(numShapes):
    randomly_draw()
