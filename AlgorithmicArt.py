#!/usr/bin/python3
import turtle
import math
import random

# get user input and change modify options 
iterations = int(input("how many iterations would you like to run (should be above 1000): "))
size = input("do you want the line size to vary [y/n]")
if(size == "n"):
    sizeYN = 0
else:
    sizeYN = 1
color = input("do you want color to vary [y/n]")
if(color == "n"):
    colorYN = 0
else:
    colorYN = 1

# initialize turtle
pendulum = turtle.Turtle()
pendulum.speed(0)
pendulum.pensize(0)
turtle.colormode(255)
# list of possible frequencies
frequencies = [1, 2, 3, 4, 5, 6, 7/2, 9/2, 15/4]
# parameter values for the pendulum
# parameters for x axis
# random frequency from list
freqX = frequencies[random.randrange(len(frequencies))]
ampX = 250
# random pahse shift, multiple of pi/2
phaseX = math.pi/2 * random.randrange(4)
dampX = 0.01
# parameters for y axis
# random frequency from list
freqY = frequencies[random.randrange(len(frequencies))]
ampY = 250
phaseY = 0
dampY = 0.0
# print the parameters
print("x frequency: " + str(freqX))
print("y frequency: " + str(freqY))
print("phase shift: " + str(phaseX))
print("iterations: " + str(iterations))

pendulum.pu()
# draw the harmonograph for selected number of iterations
for i in range(iterations):
    # change the denominator for different render detail, comes at cost of time
    timeElapsed = i/35
    # sine fuctions with damping to simulate a real pendulum
    xPos = ampX*math.sin(timeElapsed*freqX + phaseX)*math.exp(-dampX*timeElapsed) 
    yPos = ampY*math.sin(timeElapsed*freqY + phaseY)*math.exp(-dampY*timeElapsed) 
    pendulum.goto(xPos, yPos)
    pendulum.pd()
    # sine function that changes color in time with whatever frequencies are used
    blueChannel = int((0.5*math.sin(timeElapsed*freqX + phaseX) + 0.5) * 255)
    # can include following line if want to change between 4 colors instead of 2
    # greenChannel = int((0.5*math.sin(timeElapsed*freqY + phaseY) + 0.5) * 255)
    pendulum.color(0, 180, blueChannel * colorYN)
    # change pen size in time with the pendulum
    penSize = (2*math.sin(timeElapsed*freqY*2 + phaseY - math.pi/2) + 3)
    pendulum.pensize(penSize * sizeYN)


turtle.mainloop()
