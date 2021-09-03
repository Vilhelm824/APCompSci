#   a116_ladybug.py
import turtle as trtl


ladybug = trtl.Turtle()
# configure parameters for drawing legs
iterations = 6
leg_length = 50 # default 70
leg_angle = 240 / iterations
ladybug.pensize(5)
leg_index = 0
# draw legs
while (leg_index < iterations):
  ladybug.goto(0,-30)
  if(leg_index >= iterations/2):
    ladybug.setheading(leg_angle*leg_index + (90 - leg_angle) - 35)
  else:
      ladybug.setheading(leg_angle*leg_index - 35)
  ladybug.forward(leg_length)
  leg_index += 1


# create ladybug head
ladybug.pu()
ladybug.goto(0, 0)
ladybug.pd()
ladybug.setheading(0)
ladybug.pensize(40)
ladybug.speed(0)
ladybug.circle(5)

# and body
ladybug.pu()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pd()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.pu()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pd()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 35, ypos + 10)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos -= 6
  ypos += 30
  num_dots += 1


ladybug.hideturtle()
wn = trtl.Screen()
wn.mainloop()
