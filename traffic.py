#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
import math

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.speed(0)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.speed(0)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

speed = 1
steps = 0
while steps < 50:
    for i in range(len(horiz_turtles)): 
        horiz_turtles[i].speed(speed)
        vert_turtles[i].speed(speed)
        x_distance = abs(horiz_turtles[i].xcor() - vert_turtles[i].xcor())
        y_distance = abs(horiz_turtles[i].ycor() - vert_turtles[i].ycor())
        if(x_distance > 20 and y_distance > 20):
            horiz_turtles[i].fd(8)
            vert_turtles[i].fd(8)
        speed = int(5 * math.sin(steps/8) + 5)
        print(speed)
        
    steps = steps + 1



wn = trtl.Screen()
wn.mainloop()
