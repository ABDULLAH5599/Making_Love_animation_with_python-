import turtle
from turtle import *

wn= getscreen();
wn.bgcolor("cyan");

t=turtle.Turtle();
t.fillcolor('red')

t.hideturtle()
t.goto(10,-20)
turtle.pencolor("white")

t.pensize(3)
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t,goto(-65,230)
t.pendown()
t.color('white')

def write(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style=('Stencil std', 25,'bold')
    t.write(message,font=style)


write('S',(-88,110))
write('I',(-65,110))
write('F',(-55,110))
write('A',(-35,110))
write('T',(-16,110))
write('A',(10,110))
write('D',(36,110))
write('N',(60,110))
write('A',(85,110))
write('N',(110,110))
turtle.done

# t.write('SIFAT ADNAN',font=('Stencil std',25,'bold'))
turtle.done()

# # left(40)
# # forward(100)
# # circle(40,180)
#
# def curve():
#     for i in range(200):
#
#      t.rt(1)
#      t.fd(1)
#
#
# def heart():
#     t.fillcolor('red')
#     t.begin_fill()
#     t.lt(140)
#     t.fd(113)
#
#     curve()
#     t.lt(120)
#     curve()
#     t.fd(112)
#     t.end_fill();
#
# heart()
# t.ht()
#
# def write(message,pos):
#     x,y=pos
#     t.penup()
#     t.goto(x,y)
#     t.color('white')
#     style=('Stencil std', 18)
#     t.write(message,font=style)
#
#
# write('S',(-78,95))
# write('I',(-65,95))
# write('F',(-55,95))
# write('A',(-30,95))
# write('T',(-14,95))
# write('A',(10,95))
# write('D',(26,95))
# write('N',(45,95))
# write('A',(65,95))
# write('N',(80,95))
# turtle.done
# wn.mainloop()