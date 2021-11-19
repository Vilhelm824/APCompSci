import turtle

pen = turtle.Turtle()


def draw_rect(x, y, centerX, centerY, color):
  pen.fillcolor(color)
  pen.begin_fill()
  pen.pu()
  pen.goto(centerX - x / 2, centerY - y / 2)
  pen.pd()
  pen.goto(centerX - x / 2, centerY + y / 2)
  pen.goto(centerX + x / 2, centerY + y / 2)
  pen.goto(centerX + x / 2, centerY - y / 2)
  pen.goto(centerX - x / 2, centerY - y / 2)
  pen.end_fill()


def draw_circle(circleRadius, centerX, centerY, color):
  pen.pu()
  pen.goto(centerX, centerY - circleRadius)
  pen.pd()
  pen.fillcolor(color)
  pen.begin_fill()
  pen.circle(circleRadius)
  pen.end_fill()


def draw_mountain(color, centerX, bottomY):
  centerX = centerX - 100
  pen.fillcolor(color)
  pen.pu()
  pen.goto(centerX, bottomY)
  pen.pd()
  pen.begin_fill()
  pen.goto(centerX + 200, bottomY)
  pen.goto(centerX + 150, bottomY + 80)
  pen.goto(centerX + 50, bottomY + 80)
  pen.goto(centerX, bottomY)
  pen.end_fill()
  pen.fillcolor('white')
  pen.begin_fill()
  pen.goto(centerX + 50, bottomY + 80)
  pen.goto(centerX + 75, bottomY + 120)
  pen.goto(centerX + 125, bottomY + 120)
  pen.goto(centerX + 150, bottomY + 80)
  pen.goto(centerX + 50, bottomY + 80)
  pen.end_fill()


pen.pensize(3)

sunSize = input("How big is the sun (from 1-5): ")
skyColor = input("what color is the sky: ")
mountainColor = input("what color is the montain: ")
sunRadius = float(sunSize) * 5 + 10

print("ok, drawing your sunset")

draw_rect(400, 250, 0, 125, skyColor)
draw_circle(sunRadius, -5, 30, "yellow")
draw_mountain(mountainColor, -100, 0)
draw_mountain(mountainColor, 70, -20)
draw_rect(400, 50, 0, -25, "sienna")


screen = turtle.Screen()
screen.mainloop()
