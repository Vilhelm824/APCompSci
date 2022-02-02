from PIL import Image
 
im = Image.open("output.gif")
rgb_im = im.convert('RGB')      #check
 
#defines variables to maneuver encoded image message
DISTANCE_BETWEEN_BLOCKS = 21
rgb_list = []
 
#scans image by each row and converts rgb value into 0 and 1 in a list
for i in range(10, 960, DISTANCE_BETWEEN_BLOCKS):
    r,g,b = rgb_im.getpixel((i,405))
    # print(r,g,b)
    rgb_list.append(r)
    rgb_list.append(g)
    rgb_list.append(b)
 
rgb_shifted = []
 
for number in rgb_list:
    if number != 255:
        rgb_shifted.append(number>>1)
 
# print(rgb_shifted)
 
decoded = " "
for letter in rgb_shifted:
    decoded = decoded + chr(letter)
 
print("Decoded Message:", decoded)
