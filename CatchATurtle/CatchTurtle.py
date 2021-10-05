#-----import statements-----
import turtle
from random import choice, randrange
import leaderboard as lb

#-----game configuration----
screen = turtle.Screen()
turtleColor = "sky blue"
turtleShape = "turtle"
turtleSize = 2
playerScore = 0
fontSetup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
colors = ["olive drab", "light pink", "dark orchid", "sienna", "chartreuse", "coral", "light green", "khaki"]
leaderboard_file_name = "leaderboardData.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Enter your name: ")
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
        screen.bgcolor("pink")
    else:
        jeffery.ht()
        screen.bgcolor("red")



def Countdown():
  global timer, timer_up
  TimeKeeper.clear()
  if timer <= 0:
    TimeKeeper.write("Time's Up", font=fontSetup)
    timer_up = True
    manage_leaderboard()
  else:
    TimeKeeper.write("Timer: " + str(timer), font=fontSetup)
    timer -= 1
    TimeKeeper.getscreen().ontimer(Countdown, counter_interval) 


def StampColor():
    global colors
    jeffery.color(choice(colors))
    jeffery.stamp()
    jeffery.color(turtleColor)


# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  global leaderboard_file_name
  global leader_scores_list
  global leader_names_list
  global playerScore
  global jeffery

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or playerScore > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, playerScore)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, jeffery, playerScore)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, jeffery, playerScore)

#-----events----------------
jeffery.onclick(JeffWasClicked)
TimeKeeper.getscreen().ontimer(Countdown, counter_interval)

screen.mainloop()

