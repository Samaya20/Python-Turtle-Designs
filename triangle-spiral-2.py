from turtle import *

Screen().bgcolor('black')
Screen().setup(800,600)
speed(-100)
tupleColor = ('#9007ca','#01e1fd','#1234fe','#ffaf11','#fd0ec6','#0d37fe')
for i in range(450):
    pencolor(tupleColor[i%6])
    forward(i)
    right(89)
    width(2)
    forward(i * 2)
    right(89)

mainloop()    