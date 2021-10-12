import turtle
import random
import functools

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
key_list = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
apples_list = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]
turtle_list = []
num_apples = 9

wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

pen = turtle.Turtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.goto((random.randrange(-200, 200)), active_apple.ycor())
  active_apple.shape(apple_image)
  wn.update()


def Newton(active_apple):
  active_apple.pu()
  active_apple.sety(-150)
  active_apple.clear()


def DumbUser(active_apple, key):
  active_apple.color("white")
  wn.tracer(False)
  active_apple.goto(active_apple.xcor(), active_apple.ycor()-35)
  active_apple.write(key, font=("Arial", 40, "bold"), align='center')
  active_apple.goto(active_apple.xcor(), active_apple.ycor()+35)
  wn.tracer(True)


#-----function calls-----
# initiate all apples
for n in apples_list:
  apple = turtle.Turtle()
  apple.pu()
  turtle_list.append(apple)

# draw the apples
index = 0
for apple in turtle_list:
  draw_apple(apple)
  DumbUser(apple, key_list[index])
  index += 1


for i in range(9):
  wn.onkeypress(functools.partial(Newton, turtle_list[i]), key_list[i])
  

wn.listen()
wn.mainloop()