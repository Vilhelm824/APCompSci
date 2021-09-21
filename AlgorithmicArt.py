#!/usr/bin/pytin3
import turtle
import math
import time

pendulum = turtle.Turtle()
pendulum.speed(0)
# parameter values for the pendulum
# parameters for x axis
freqX = 7
ampX = 200
phaseX = math.pi/2 * 0
dampX = 0.01
# parameters for y axis
freqY = 4
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

turtle.mainloop()