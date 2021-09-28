#-----import statements-----
import turtle
from random import randrange

#-----game configuration----
screen = turtle.Screen()
turtleColor = "sky blue"
turtleShape = "turtle"
turtleSize = 2
playerScore = 0
fontSetup = ("Arial", 20, "normal")
#-----initialize turtle-----
jeffery = turtle.Turtle()
ScoreKeeper = turtle.Turtle()
jeffery.color(turtleColor)
jeffery.shape(turtleShape)
jeffery.turtlesize(turtleSize)
jeffery.pu()
ScoreKeeper.pu()
ScoreKeeper.ht()
ScoreKeeper.goto(-400, 350)

#-----game functions--------
def ChangePosition():
    randX = randrange(-400, 400)
    randY = randrange(-350, 350)
    jeffery.goto(randX, randY)


def UpdateScore():
    global playerScore
    playerScore += 1
    ScoreKeeper.clear()
    ScoreKeeper.write(playerScore, font=fontSetup)


def JeffWasClicked(x, y):
    ChangePosition()
    UpdateScore()


#-----events----------------
jeffery.onclick(JeffWasClicked)

screen.mainloop()
