import turtle

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
keyList = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]

wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

pen = turtle.Turtle()
apple = turtle.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()


def Newton(active_apple = apple):
  active_apple.pu()
  active_apple.goto(active_apple.xcor(), -150)
  active_apple.clear()


def DumbUser(active_apple):
  active_apple.color("white")
  active_apple.pu()
  wn.tracer(False)
  active_apple.goto(active_apple.xcor(), active_apple.ycor()-35)
  active_apple.write("A", font=("Arial", 40, "bold"), align='center')
  active_apple.goto(active_apple.xcor(), active_apple.ycor()+35)
  wn.tracer(True)


#-----function calls-----
draw_apple(apple)
DumbUser(apple)

wn.onkeypress(Newton, "a")

wn.listen()
wn.mainloop()