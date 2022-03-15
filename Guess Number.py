from turtle import *
import random

colormode(255)
pensize(20)
shape('turtle')
turtle_screen = getscreen()
turtle_screen.bgcolor(0,0,0)

secret_number = random.randrange(1,10)
guess_number = numinput("Guess!", "Guess a number", "", 1, 10)


def drawUpArrow():
    left(90)
    pencolor(250,100,50)
    forward(100)
    backward(100)
    right(90)

def drawDownArrow():
    right(90)
    pencolor(250,30,30)
    forward(100)
    backward(100)
    left(90)

def drawCheck():
    pencolor(30,250,20)
    for i in range(10):
        left(36)
        forward(50)
        backward(50)

while secret_number != guess_number:
    clear()
    if guess_number > secret_number:
        drawDownArrow()
    else:
        drawUpArrow()
    guess_number = numinput("Guess Again!", "Wrong! Guess a number", "", 1, 10)
clear()
drawCheck()
