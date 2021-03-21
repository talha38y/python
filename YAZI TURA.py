import random, time, turtle, os
from playsound import playsound

win = turtle.Screen()
win.screensize(1280, 720)
win.title('Yazı Tura')
win.bgcolor('blue')
win.bgpic('C:/Users/talha/Desktop/uygulama/duva.gif')
win.tracer(2)

turtle.register_shape('C:/Users/talha/Desktop/uygulama/el.gif')
turtle.register_shape('C:/Users/talha/Desktop/uygulama/yazı.gif')
turtle.register_shape('C:/Users/talha/Desktop/uygulama/tura.gif')

para = turtle.Turtle()
para.color('blue')
para.shape('C:/Users/talha/Desktop/uygulama/el.gif')
para.penup()
para.goto(0, 0)

def at():
    a=random.randint(1, 2)
    if a==1:
        time.sleep(1)
        para.shape('C:/Users/talha/Desktop/uygulama/yazı.gif')
    else:
        time.sleep(1)
        para.shape('C:/Users/talha/Desktop/uygulama/tura.gif')

win.listen()
win.onkey(at, 'space')
