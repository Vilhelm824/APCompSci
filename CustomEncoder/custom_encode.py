import turtle as trtl
from PIL import ImageGrab, Image, ImageDraw

message = input("Message: ")


pen = trtl.Turtle()
trtl.colormode(255)


# character to unicode
unicode = []
for character in message:
    unicode.append(ord(character))
# print(unicode)

# unicode bit shift
bit_shifted = []
for number in unicode:
    bit_shifted.append(number<<1)

# make length multiple of 3
while((len(bit_shifted)%3) != 0):
    bit_shifted.append(0)

# print(bit_shifted)

# convert to rgb
rgb_list = []
for i in range(0, int(len(bit_shifted)/3)):
    rgb_list.append([bit_shifted[3*i], bit_shifted[3*i+1], bit_shifted[3*i+2]])
# print(rgb_list)


# setup turtle
pen.penup()
pen.goto(-450,0)
pen.setheading(0)
pen.shape("square")
# pen.pensize(5)

for n in range(0,len(rgb_list)):
    pen.color(rgb_list[n][0], rgb_list[n][1], rgb_list[n][2])
    pen.fd(21)
    pen.stamp()

# take a screenshot of the turtle output
screen = pen.getscreen()
root = trtl.getcanvas().winfo_toplevel()
root.call('wm', 'attributes', '.', '-topmost', '1')  # credit to cdlane on stack overflow

def create_image(widget):
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    x1=x+widget.window_width()
    y1=y+widget.window_height()
    im = ImageGrab.grab().crop((x,y,x1,y1))
    im.save("output.gif")
    # print(im.size) 


create_image(screen)