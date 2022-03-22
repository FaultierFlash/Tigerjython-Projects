from gturtle import *
import time as t
#import N_Eck
#import DasHausvomNikolaus
#import variablesSchachbrett

S = 1000        #Die Geschwindigkeit der Schildkröte
TC = 'green'    #Die Farbe der Schildkröte
PC = 'black'    #Die Farbe der Linien
MC = 'black'    #Die erste Feld-Farbe
SC = 'blue'     #Die zweite Feld-Farbe
HT = False      #HideTurtle an oder aus (versteckt die Schildkröte und alles wird sofort gezeichnet)
Xv = 10         #Die Breite des Schachbretts in Feldern
Yv = 10         #Die Höhe des Schachbretts in Feldern
restart = True  #Schaut ob Schon auf die neustart Taste gedrückt wurde

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
    
def n_eck(N):
    
    
        
    A = 360/N
    

    setX(-(getPlaygroundWidth()/2*0.8))
    setY(-1500/N*0.5)
    
    repeat N:
        fd(1500/N)
        right(A)
    

def schachfeld(Xv, Yv):
    Fy = True
    Fx = True
    
    Xs = getPlaygroundWidth()*0.9/Xv
    Ys = getPlaygroundHeight()*0.9/Yv
    
    if Ys < Xs:
        size = Ys
        
    else:
        size = Xs

    setPos(-0.9*getPlaygroundWidth()/2, -0.9*getPlaygroundHeight()/2)
    
    repeat Xv:
        if Fx:
            Fy = True
            Fx = False
        else:
            Fy = False
            Fx = True
            
        repeat Yv:
            repeat 4:
                fd(size)
                rt(90)
                
            if Fy:
                Fy = False
                P = getPos()
                
                setPos(P[0]+0.5*size, P[1]+0.5*size)
                
                setFillColor(MC)
                fill()
                
                setPos(P[0], P[1])
                
            else:
                Fy = True
                P = getPos()
                
                setPos(P[0]+0.5*size, P[1]+0.5*size)
                
                setFillColor(SC)
                fill()
                
                setPos(P[0], P[1])
                
            fd(size)
            
        setPos(getX()+size, getY()-size*Yv)
    

while True:
    if restart == False:
        break
    
    elif restart == None:
        continue
        
    restart = None 
    cs()
    
    Selection = inputInt('Wähle ein Programm: \n 1) Das Haus vom Nikolaus \n 2) N-Eck \n 3) Variables Schachbrett \n 4) To be continued...')
    
    if Selection == 1:
        size = inputInt('Welche Größe soll das Haus haben?')
        HT = askYesNo('Soll HideTurtle aktiv sein?')

        if  HT == False:
            st()
            S = inputInt('Wie schnell soll die Turte Sein?')
            TC = askColor('Welche Farbe sollen die Turtle haben?', 'green' )    #inputString('Welche Farbe soll die Turtle haben?')
        
        PC = askColor('Welche Farbe sollen die Linien haben?', 'black' )        #inputString('Welche Farbe sollen die Linien haben?')
        
        setColor(TC)
        setPenColor(PC)
        speed(S)
        
        if HT:
            ht()
            
        HausvomNikolaus(size)
    
    elif Selection == 2:
        N = inputInt('Wie viele Ecken Soll das N-Eck haben?')
        HT = askYesNo('Soll HideTurtle aktiv sein?')
        
        if  HT == False:
            S = inputInt('Wie schnell soll die Turte Sein?')
            TC = askColor('Welche Farbe sollen die Turtle haben?', 'green' )    #inputString('Welche Farbe soll die Turtle haben?')
            st()
        
        PC = askColor('Welche Farbe sollen die Linien haben?', 'black' )        #inputString('Welche Farbe sollen die Linien haben?')
        
        speed(S)
        setPenColor(PC)
        setColor(TC)
        
        if HT == True:
            ht()
            
        n_eck(N)
        
    elif Selection == 3:
        Xv = inputInt('Wie viele Felder Soll das Schachbrettmuster breit sein?')
        Yv = inputInt('Wie viele Felder Soll das Schachbrettmuster hoch sein?')
        
        HT = askYesNo('Soll HideTurtle aktiv sein?')
        
        if  HT == False:
            st()
            S = inputInt('Wie schnell soll die Turte Sein?')
            TC = askColor('Welche Farbe sollen die Turtle haben?', 'green' )    #inputString('Welche Farbe soll die Turtle haben?')
        
        PC = askColor('Welche Farbe sollen die Linien haben?', 'black' )        #inputString('Welche Farbe sollen die Linien haben?')
        MC = askColor('Was soll sie erste Farbe sein?', 'black' )               #inputString('Was soll die erste Farbe sein?')
        SC = askColor('Was soll die zweite Farbe sein?', 'white' )              #inputString('Was soll die zweite Farbe sein?')
        
        setColor(TC)
        setPenColor(PC)
        setFillColor(MC)
        speed(S)
                
        if HT:
            ht()
        
        schachfeld(Xv, Yv)
        
    else:
        continue
        
    t.sleep(5)
    
    restart = askYesNo('Willst du zurück zum Anfang?')
    

