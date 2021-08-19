import turtle

pen = turtle.Turtle()

# haha this is the messiest code ever but that's because i made a bunch 
# of methods so the actual execution script is readable and it would
# take way too much time and be overkill to rewrite everything :)
def draw_rect(x, y, centerX, centerY):
  pen.pu()
  pen.goto(centerX - x / 2, centerY - y / 2)
  pen.pd()
  pen.goto(centerX - x / 2, centerY + y / 2)
  pen.goto(centerX + x / 2, centerY + y / 2)
  pen.goto(centerX + x / 2, centerY - y / 2)
  pen.goto(centerX - x / 2, centerY - y / 2)


def draw_parallelogram(x, y, leftCornerX, leftCornerY, offset):
  pen.pu()
  pen.goto(leftCornerX, leftCornerY)
  pen.pd()
  pen.goto(leftCornerX + x, leftCornerY)
  pen.goto(leftCornerX + x + offset, leftCornerY - y)
  pen.goto(leftCornerX + offset, leftCornerY - y)
  pen.goto(leftCornerX, leftCornerY)
  
# draw depth for the computer  
def depth_lol():
  pen.pu()
  pen.goto(-100, -62.5)
  pen.pd()
  pen.goto(-130, -62.5)
  pen.goto(-130, 0)
  pen.goto(-100, 62.5)
  
  
def draw_key_row(rowY, rowX):
  for i in range(0, 8):
    draw_parallelogram(15, 12, rowX, rowY, 6.2)
    rowX += 22

# basically nested loop
def draw_keys():
  keyY = -90
  keyX = -82
  for j in range(0,3):
    draw_key_row(keyY, keyX)
    keyY -= 15
    keyX += 6.2


# actual function calling here
draw_rect(200, 125, 0, 0)
draw_rect(180, 105, 0, 0)
draw_parallelogram(180, 50, -90, -85, 20)
depth_lol()
draw_keys()
wn = trtl.Screen()
wn.mainloop()

