from gturtle import *

S = 1000
TC = 'green'
PC = 'black'
HT = False

makeTurtle()

def n_eck(N):
    
    
        
    A = 360/N
    

    setX(-(getPlaygroundWidth()/2*0.8))
    setY(-1500/N*0.5)
    
    repeat N:
        fd(1500/N)
        right(A)
    

N = inputInt('Wie viele Ecken Soll das N-Eck haben?')
HT = askYesNo('Soll HideTurtle aktiv sein?')

if  HT == False:
    S = inputInt('Wie schnell soll die Turte Sein?')
    TC = inputString('Welche Farbe soll die Turtle haben?')

PC =inputString('Welche Farbe sollen die Linien haben?')

speed(S)
setPenColor(PC)
setColor(TC)

if HT == True:
    ht()

if __name__ == '__main__':
    n_eck(N)

