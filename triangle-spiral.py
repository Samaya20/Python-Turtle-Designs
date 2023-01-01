from turtle import *

sides = 3
colors = ["#2600FF","#FF00FF","#B8FF00"]

tracer(5)
speed(5)
delay(0)
hideturtle()
bgcolor("black")

for i in range(500):
    color(colors[i % len(colors)])
    fd(i * 3 // sides + i)
    lt(360 / sides + 1)
    width(i * sides / 250)

done()
