#-----import statements-----
import turtle
from random import choice, randrange

#-----game configuration----
screen = turtle.Screen()
turtleColor = "sky blue"
turtleShape = "turtle"
turtleSize = 2
playerScore = 0
fontSetup = ("Arial", 20, "normal")
timer = 20
counter_interval = 1000   #1000 represents 1 second
timer_up = False
colors = ["olive drab", "light pink", "dark orchid", "sienna", "chartreuse", "coral", "light green", "khaki"]
#-----initialize turtle-----
jeffery = turtle.Turtle()
ScoreKeeper = turtle.Turtle()
TimeKeeper = turtle.Turtle()
jeffery.color(turtleColor)
jeffery.shape(turtleShape)
jeffery.turtlesize(turtleSize)
jeffery.speed(9)
jeffery.pu()
ScoreKeeper.pu()
ScoreKeeper.ht()
ScoreKeeper.speed(0)
TimeKeeper.pu()
TimeKeeper.ht()
TimeKeeper.speed(0)
ScoreKeeper.goto(-400, 350)
TimeKeeper.goto(350, 350)

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
    if not timer_up:
        ChangePosition()
        UpdateScore()
        StampColor()
        screen.bgcolor("medium spring green")
    else:
        jeffery.ht()
        screen.bgcolor("magenta")



def Countdown():
  global timer, timer_up
  TimeKeeper.clear()
  if timer <= 0:
    TimeKeeper.write("Time's Up", font=fontSetup)
    timer_up = True
  else:
    TimeKeeper.write("Timer: " + str(timer), font=fontSetup)
    timer -= 1
    TimeKeeper.getscreen().ontimer(Countdown, counter_interval) 


def StampColor():
    global colors
    jeffery.color(choice(colors))
    jeffery.stamp()
    jeffery.color(turtleColor)

#-----events----------------
jeffery.onclick(JeffWasClicked)
TimeKeeper.getscreen().ontimer(Countdown, counter_interval)

screen.mainloop()

