from gturtle import *
tf = TurtleFrame()

def onTurtleHit(t, x, y):
    t.fd(25)
    #v.fd(-25)
    print(t)
    playTone(('e', 1500), instrument= 'piano', volume = 100)


t = Turtle(tf, turtleHit = onTurtleHit)
v = Turtle(tf)
v.fd(-25)
v = Turtle(tf, turtleHit = onTurtleHit)

