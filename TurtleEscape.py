import turtle
import random
 
 
# variables
maze_width = 20
num_walls = 35
turtle_color = "magenta"
# turtle initiation
maze = turtle.Turtle()
maze.ht()
maze.color(turtle_color)
maze.pensize(8)
maze.speed(0)
maze_runner = turtle.Turtle()
maze_runner.color("blue")
maze_runner.shape("classic")
maze_runner.speed(0)
screen = turtle.Screen()
 
 
# function definitions
def DrawBarrier(location):
    maze.fd(location)
    maze.right(90)
    maze.fd(maze_width*2)
    maze.bk(maze_width*2)
    maze.right(270)
 
 
def DrawDoor(location):
    maze.fd(location)
    maze.pu()
    maze.forward(maze_width)
    maze.pd()
 
 
def RandomizeMaze(length, width):
    which_first = random.randrange(2)
    barrier_location = 0
    door_location = 0
    if(which_first == 1):
        barrier_location = random.randrange(2*width, length - 2*width, 10)
        door_location = random.randrange(0, length - width - barrier_location, 10)
    elif(which_first == 0):
        door_location = random.randrange(width, length - 2*width, 10)
        barrier_location = random.randrange(0, length - 2*width - door_location, 10)
    random_dict = {
            "barrier": barrier_location,
            "door": door_location,
            "which": which_first,
            "dist_left": length - barrier_location - door_location
        }
    return random_dict
 
 
def RunUp():
    maze_runner.seth(90)
    maze_runner.fd(3)
 
 
def RunDown():
    maze_runner.seth(270)
    maze_runner.fd(3)
 
 
def RunRight():
    maze_runner.seth(0)
    maze_runner.fd(3)
 
 
def RunLeft():
    maze_runner.seth(180)
    maze_runner.fd(3)
 
 
# draw maze
maze_runner.pu()
maze_runner.goto(maze_width * 3, -3 * maze_width)
maze_runner.pd()
 
for i in range(num_walls):
    if(i<=4):
        continue
    wall_length = i * maze_width
    random_output = RandomizeMaze(wall_length, maze_width)
    if(random_output["which"] == 1):
        DrawBarrier(random_output["barrier"])
        DrawDoor(random_output["door"])
        maze.fd(random_output["dist_left"])
    elif(random_output["which"] == 0):
        DrawDoor(random_output["door"])
        DrawBarrier(random_output["barrier"])
        maze.fd(random_output["dist_left"])
    maze.right(90)
 
# game loop
screen.onkeypress(RunUp, "w")
screen.onkeypress(RunDown, "s")
screen.onkeypress(RunLeft, "a")
screen.onkeypress(RunRight, "d")
 
screen.listen()
screen.mainloop()
