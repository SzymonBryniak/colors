import colorgram as cg

colorsExtracted = []
colors = cg.extract('image.jpg', 10)
print(colors[0].rgb)


for i in range(len(colors)):
    Append = colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b
    colorsExtracted.append(Append)
#com
print(colorsExtracted)

import turtle as t
import random as rn
                        #TODO:20 dots spaced by 50
screen = t.Screen()
screen.colormode(255)
colorList = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]


t.penup()
for i in range(10):
    t.setpos(-200, 50*i)
    for c in range(10):
        ranColor = rn.choice(colorList)
        t.forward(50)
        t.dot(20, ranColor)

screen.exitonclick()

