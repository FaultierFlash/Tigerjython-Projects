from gturtle import *

TC = 'green' #Die Farbe der Schildkröte
PC = 'black' #Die Farbe der Linien

S = 1000 #Die Geschwindigkeit der Schildkröte

makeTurtle()

def HausvomNikolaus(size):
    
    setPos(-0.75*(getPlaygroundWidth()/2), -0.75*(getPlaygroundHeight()/2))
    setFramePositionCenter()
    
    forward(size)
    right(45)
    forward(sqrt(size ** 2/2)) 
    right(90)
    forward(sqrt(size ** 2/2)) 
    right(135)
    forward(size)
    left(135)
    forward(sqrt(2*size ** 2))
    right(135)
    forward(size)
    right(135)
    forward(sqrt(2*size ** 2))
    right(135)
    forward(size)
  


size = inputInt('Welche Größe soll das Haus haben?')
HT = askYesNo('Soll HideTurtle aktiv sein?')

if  HT == False:
    S = inputInt('Wie schnell soll die Turte Sein?')
    TC = inputString('Welche Farbe soll die Turtle haben?')

PC =inputString('Welche Farbe sollen die Linien haben?')
    
setColor(TC)
setPenColor(PC)
speed(S)

if HT:
    ht()

if __name__ == '__main__':
    HausvomNikolaus(size)

    
    
