import turtle
import os
import time
# from PIL import Image

# Clearing the Screen
os.system('cls')

t = turtle.Turtle()

# Background Color
# turtle.bgcolor('#87CEEB')  # Light sky color
# Earth Tones: Various shades of brown and gray, such as #8B4513 (saddle brown) or #808080 (gray).
# Subdued Green: #556B2F
# Deep Blue or Navy: #000080
# Off-White or Cream: #F5F5F5
# Soft Gold or Light Yellow: #FFD700
# Sunset Palette:
#
# Saffron: #FFA500
# Green: #008000
# Blue: #6A5ACD (Slate Blue)
# Background: A gradient or blend of colors inspired by a sunset, transitioning from warm oranges to deep purples.
# Nature-inspired Palette:
#
# Saffron: #FF8C00  //Tasted
# Green: #006400
# Blue: #00CED1 (Dark Turquoise)  //Tasted
# Background: A calming shade of teal or aqua, representing the sky and water, which can complement the other vibrant flag colors.
# Jewel Tones Palette:
#
# Saffron: #FF4500 (Orange Red)
# Green: #008080 (Teal)  //Tested
# Blue: #4B0082 (Indigo)
# Background: A rich, dark purple or violet that complements the jewel tones of the flag.
# Desert Sands Palette:
#
# Saffron: #FFA500
# Green: #228B22 (Forest Green)
# Blue: #4682B4 (Steel Blue)
# Background: A warm desert sand color that contrasts with the other colors, evoking the Indian landscape.
# Mystical Twilight Palette:
#
# Saffron: #FF6347 (Tomato)
# Green: #228B22 (Forest Green)
# Blue: #8A2BE2 (Blue Violet)
# Saffron: #FFA500

# Elegant Minimalism:
#
# Saffron: #FFA500
# White: #FFFFFF
# Green: #008000
# Blue: #000080
# Background: A clean and modern background with a gradient of muted shades of saffron, white, and green, transitioning to a deep blue at the bottom.
# Celestial Harmony:
#
# Saffron: #FF8C00
# White: #FFFFFF
# Green: #006400
# Blue: #0000CD (Medium Blue)
# Background: A cosmic-inspired background with a deep blue sky adorned with subtle stars and a gentle glow, representing unity and harmony.
# Lively Fusion:
#
# Saffron: #FF4500 (Orange Red)
# White: #FFFFFF
# Green: #008080 (Teal)
# Blue: #4B0082 (Indigo)
# Background: A dynamic and vibrant background with swirling gradients that blend the flag's colors, creating a lively and energetic atmosphere.
# Cultural Elegance:
#
# Saffron: #FF6347 (Tomato)
# White: #FFFFFF
# Green: #228B22 (Forest Green)
# Blue: #8A2BE2 (Blue Violet)
# Background: An artistic background featuring intricate patterns inspired by Indian art and culture, incorporating the flag's colors in a sophisticated manner.
# Serene Landscapes:
#
# Saffron: #FFA500
# White: #F5F5F5
# Green: #006400
# Blue: #4682B4 (Steel Blue)
# turtle.bgcolor('#RRGGBB')
# turtle.setfillopacity(50)
# screen = turtle.Screen()
# screen.setup(1895, 1080)
# turtle.bgcolor('#4682B4')

# im = Image.open("drawing.eps")
# im.save("drawing.png", "PNG", transparency=255)

# canvas = screen.getcanvas()
# canvas.postscript(file="drawing.eps")

# Elegant Minimalism:
#
#
# Background: A clean and modern background with a gradient of muted shades of saffron, white, and green, transitioning to a deep blue at the bottom.
# Celestial Harmony:
#
# Saffron: #FF8C00
# White: #FFFFFF
# Green: #006400
# Blue: #0000CD (Medium Blue)
# Background: A cosmic-inspired background with a deep blue sky adorned with subtle stars and a gentle glow, representing unity and harmony.
# Lively Fusion:
#
# Saffron: #FF4500 (Orange Red)
# White: #FFFFFF
# Green: #008080 (Teal)
# Blue: #4B0082 (Indigo)
# Background: A dynamic and vibrant background with swirling gradients that blend the flag's colors, creating a lively and energetic atmosphere.
# Cultural Elegance:
#
# Saffron: #FF6347 (Tomato)
# White: #FFFFFF
# Green: #228B22 (Forest Green)
# Blue: #8A2BE2 (Blue Violet)
# Background: An artistic background featuring intricate patterns inspired by Indian art and culture, incorporating the flag's colors in a sophisticated manner.
# Serene Landscapes:
#
# Saffron: #FFA500
# White: #F5F5F5
# Green: #006400
# Blue: #4682B4 (Steel Blue)
# turtle.bgcolor('black')




length = 600
width = (length/2)/2
angle = 90

rot = 24
stick = 50
#

green = '#046A38'
saffron = '#FF671F'
# blue = '06038D'
# white = '#FFFFFF'


# for turtle in screen.turtles():
#     screen.window_height(400)
#
#     screen.window_width(600)
def cir():  # The circulation for the ASHOKA
    for j in range(5):
        t.rt(1)
        t.fd(1)


def line():  # Lining in between ASHOKA
    # t.goto(100,None)
    t.rt(angle)
    t.fd(stick)
    t.bk(stick)


def ashok():  # Ashok-Chakra
    # For the position of the Ashok-Chakra
    # t.speed(0)
    t.fd(length/2 + 50)
    t.rt(angle)
    t.fd(width/2)
    t.pensize(3)
    t.pencolor('blue')

    # Drawing the Ashok-Chakra
    for i in range(rot):
        t.rt(10)
        # t.pensize(2)
        t.fd(8)
        cir()
        line()
        t.lt(angle)

    t.lt(90)
    t.fd(3)
    t.pencolor('white')
    # t.fd(3)
    t.rt(90)
    # Back to the Position
    t.pencolor('white')
    t.bk(width/2 + 3)
    # t.bk(width - rem)
    t.lt(angle)
    t.bk(length/2 + 53)
#     t.goto(0,5)


def box():
    for i in range(2):
        t.fd(length)
        t.rt(angle)
        t.fd(width)
        t.rt(angle)


def layer():
    t.lt(angle)
    t.pendown()
    t.fd(width)
    t.rt(angle)


t.pensize(3)
def flag():  # Flag drawing
    # For the green box
    t.begin_fill()
    t.bk(width*2)
    t.color(green)
    box()
    t.end_fill()  # Green box close

    # For the white box
    t.begin_fill()
    t.color('white')
    layer()
    box()
    t.end_fill()  # White box close
    ashok()

    # For the Saffron box
    t.begin_fill()
    t.color(saffron)
    # t.color('red')
    layer()
    box()
    t.end_fill()  # Saffron box close


time.sleep(3)
flag()
t.hideturtle()
# while(True):
#     os.system('cls')
#     os.system('cls')
#     os.system('cls')
turtle.done()