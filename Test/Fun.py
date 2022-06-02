from os import curdir
from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range (1200):
    color('red')
    circle(i*.3)
    color('blue')
    circle(i*.5)
    color('green')
    circle(i)
    right(3)
    forward(3)
done()