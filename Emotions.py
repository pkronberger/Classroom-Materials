from turtle import *
shape("turtle")

def smile():
    #face background
    penup()
    goto(0,-150)
    pendown()
    begin_fill()
    color("black","yellow")
    pensize(5)
    circle(150)
    end_fill()


    #smile
    penup()
    goto(-100,0)
    right(90)
    pendown()
    color("purple")
    circle(100,180)
    #left eye
    penup()
    goto(-40,50)
    pendown()
    begin_fill()
    color("white", "green")
    circle(20)
    end_fill()
    #right eye
    penup()
    goto(80,50)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    home()

def frown():
    #face background
    penup()
    right(90)
    fd(150)
    pendown()
    begin_fill()
    color("black","blue")
    pensize(5)
    left(90)
    circle(150)
    end_fill()
    #smile
    penup()
    goto(100,-100)
    left(90)
    pendown()
    color("purple")
    circle(100,180)
    right(180)
    #left eye
    penup()
    goto(-40,50)
    pendown()
    begin_fill()
    color("white", "green")
    circle(20)
    end_fill()
    #right eye
    penup()
    goto(80,50)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    home()

def howAreYou():
    feeling = textinput("Feels","Are you in a good mood today?")
    if feeling == "yes":
        smile()
    elif feeling == "no":
        frown()
    else:
        print("You entered : " + feeling + ". Please enter yes or no")
        howAreYou()

howAreYou()
