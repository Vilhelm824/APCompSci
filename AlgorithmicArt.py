#!/usr/bin/pytin3
import turtle
import math
import time

pendulum = turtle.Turtle()
pendulum.speed(0)
# parameter values for the pendulum
# parameters for x axis
freqX = 10
ampX = 400
phaseX = 0
dampX = 0.5
freqX1 = 8
ampX1 = 100
phaseX1 = 0
dampX1 = 0.01
# parameters for y axis
freqY = 10
ampY = 400
phaseY = 0
dampY = 0.5
freqY1 = 10
ampY1 = 100
phaseY1 = 0
dampY1 = 0.01

# initial time
startTime = time.time()

for i in range(1000):
    timeElapsed = time.time() - startTime

    xPos = ampX*math.sin(timeElapsed*freqX + phaseX)*math.exp(-dampX*timeElapsed) + ampX1*math.sin(timeElapsed*freqX1 + phaseX1)*math.exp(-dampX1*timeElapsed)
    yPos = ampY*math.sin(timeElapsed*freqY + phaseY)*math.exp(-dampY*timeElapsed) + ampY1*math.sin(timeElapsed*freqY1 + phaseY1)*math.exp(-dampY1*timeElapsed)
    
    pendulum.goto(xPos, yPos)

    print(xPos)

turtle.mainloop()