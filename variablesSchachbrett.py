from gturtle import *

S = 1000        #Die Geschwindigkeit der Schildkröte
TC = 'green'    #Die Farbe der Schildkröte
PC = 'black'    #Die Farbe der Linien
MC = 'black'    #Die erste Feld-Farbe
SC = 'blue'     #Die zweite Feld-Farbe
HT = False      #HideTurtle an oder aus (versteckt die Schildkröte und alles wird sofort gezeichnet)
Xv = 10         #Die Breite des Schachbretts in Feldern
Yv = 10         #Die Höhe des Schachbretts in Feldern

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
    

if __name__ == '__main__':
    makeTurtle()
    
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