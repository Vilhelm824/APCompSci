#!/usr/bin/python3
import turtle
import math
import time

pendulum = turtle.Turtle()
pendulum.speed(0)
pendulum.pensize(2)
turtle.colormode(255)
# parameter values for the pendulum
# parameters for x axis
freqX = 3
ampX = 200
phaseX = math.pi/2 * 0
dampX = 0.01
# parameters for y axis
freqY = 7
ampY = 200
phaseY = 0
dampY = 0.01

# initial time
startTime = time.time()
pendulum.pu()
for i in range(5000):
    timeElapsed = time.time() - startTime

    xPos = ampX*math.sin(timeElapsed*freqX + phaseX)*math.exp(-dampX*timeElapsed) 
    yPos = ampY*math.sin(timeElapsed*freqY + phaseY)*math.exp(-dampY*timeElapsed) 
    pendulum.goto(xPos, yPos)
    pendulum.pd()

    blueChannel = int((0.5*math.sin(timeElapsed*freqX + phaseX) + 0.5) * 255)
    # can include if want to change between 4 colors instead of 2
    # greenChannel = int((0.5*math.sin(timeElapsed*freqY + phaseY) + 0.5) * 255)
    pendulum.color(0, 180, blueChannel)


turtle.mainloop()
