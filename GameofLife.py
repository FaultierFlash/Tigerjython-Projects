from gturtle import * 
import time as t            #time wird benötigt um einfach die zeit zu messen
from copy import deepcopy   #deepcopy wird benötigt um verschachtelte Listen kopieren zu können

S = 1000        #Die Geschwindigkeit der Schildkröte
TC = 'green'    #Die Farbe der Schildkröte
PC = 'grey'     #Die Farbe des Grids
MC = 'black'    #Die Farbe aktiver Felder
SC = 'white'    #Die Farbe inaktiver Felder
HT = False      #HideTurtle an oder aus (versteckt die Schildkröte und alles wird sofort gezeichnet)
Xv = inputInt("Breite des Spielfeldes in Quadraten: ")      #Die Breite des Spielfelds in Feldern
Yv = inputInt("Höhe des Spielfeldes in Quadraten: ")        #Die Höhe des SpielFelds in Feldern
Xc = 0      #Die actuelle X iteration in einer funktion
Yc = 0      #Die actuelle Y iteration in einer funktion
Iv = 0      #Die aktuelle Generation des GameOfLifes
MI = 10000  #Wie viele Iterationen soll das Game of life laufen
x, y = getScreenSize()  #Die X und Y Größe des Turtle Fensters in pixeln
x /= 1.1    #Die X-Ausdehnung des Turtlefensters wird festgelegt (Je näher der Dividend an 1 ist desto größer ist das Turtlefenster)
y /= 1.1    #Die Y-Ausdehnung des Turtlefensters wird festgelegt (Je näher der Dividend an 1 ist desto größer ist das Turtlefenster)

makeTurtle()    #Die Turtle wird erzeugt
ht()            #Die Turtle wird versteckt
setPenColor(PC) #Die Stifftfarbe wird festgesetzt

setPlaygroundSize(int(x), int(y))   #Die Spielfeldgröße wird anhand der vorher ermittelten Werte festgelegt

I = [       #I ist die Liste, die die Matrix mit all den informationen welche Zelle lebt. sie enthält außerdem jede vorherige Iteration
[
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
]

def getsize(Xv, Yv):   #size definiert die maximale Feldgröße bei Xv X Yv Feldern die ohne verzehrungen in das Turtlefensters passt
    Xs = getPlaygroundWidth()*0.9/Xv    #Xs ist die maximale Feldgröße bei Xv Feldern die in die Breite des Turtlefensters passt
    Ys = getPlaygroundHeight()*0.9/Yv   #Ys ist die maximale Feldgröße bei Yv Feldern die in die Höhe des Turtlefensters passt
    
    if Ys < Xs:     
        s = Ys
        
    else:
        s = Xs
    
    return(s)


def spielfeld(Xv, Yv):      #spielfeld zeichnet ein Gitter mit der Ausdehnung Xv Felder X Yv Felder wobei sich das Gitter unabhängig seiner Feldanzahl an die Größe des Turtlefensters anpasst
    
    Xc = 0      #Die actuelle X iteration in einer funktion
    Yc = 0      #Die actuelle Y iteration in einer funktion
    
    size = 0
    
    size = getsize(Xv, Yv)     #size ist das Ergebniss der funktion size()

    setPos(-0.9*getPlaygroundWidth()/2, -0.9*getPlaygroundHeight()/2)   #setzt die Turtle Startposition fest
    
    repeat Xv:
        Yc = Yv - 1 
        
        repeat Yv:
            repeat 4:
                fd(size)
                rt(90)
                
            fd(size)
            
            Yc -= 1
            
        setPos(getX()+size, getY()-size*Yv)
        Xc += 1
        
    setFillColor("darkgreen")    
    setPos(getPlaygroundWidth()/2*0.9, getPlaygroundHeight()/2*0.9)    
    fill()
    

def gameoflife(I, MI, Xv, Yv):
    
    St = False
    
    Xc = 0
    Yc = 0
    
    size = getsize(Xv, Yv)

    Iv = 0
    
    T = 0.00
    Tc = 0.00
    
    spielfeld(Xv, Yv)
    
    repeat MI:
        T = t.time()
        
        Sp = [-0.9*getPlaygroundWidth()/2, -0.9*getPlaygroundHeight()/2]
        
        Iv = Iv + 1
        
        Ih = deepcopy(I[Iv - 1])
        I.append(Ih)
        
        Yc = 0
        
        repeat Yv:
            Xc = 0
            
            repeat Xv:
                N = 0
                
                if Yc != 0 :
                    N = I[Iv - 1][Yc - 1][Xc] + N
                    
                    if Xc != 0:
                        N = I[Iv - 1][Yc - 1][Xc - 1] + N
                        
                    if Xc != Xv - 1:
                        N = I[Iv - 1][Yc - 1][Xc + 1] + N
                        
                
                if Yc != Yv - 1 :
                    N = I[Iv - 1][Yc + 1][Xc] + N
                    
                    if Xc != 0:
                        N = I[Iv - 1][Yc + 1][Xc - 1] + N
                        
                    if Xc != Xv - 1:
                        N = I[Iv - 1][Yc + 1][Xc + 1] + N
                        
                    
                if Xc != 0:
                    N = I[Iv - 1][Yc][Xc - 1] + N
                
                if Xc != Xv - 1:
                    N = I[Iv - 1][Yc][Xc + 1] + N
                    
                    
                if N < 2:
                    I[Iv][Yc][Xc] = 0
                    
                elif N == 3:
                    I[Iv][Yc][Xc] = 1
                 
                elif N == 2 and not I[Iv - 1][Yc][Xc] == 1:
                    I[Iv][Yc][Xc] = 0
                   
                elif N > 3:
                    I[Iv][Yc][Xc] = 0
                    
                if I[Iv][Yc][Xc] != I[Iv - 1][Yc][Xc] or Iv == 1 and I[Iv][Yc][Xc] == 1:
                    setPos(Sp[0]+Xc*size+0.5*size, Sp[1]+Yv*size-Yc*size-0.5*size)
                    
                    if I[Iv][Yc][Xc] == 1:
                        setFillColor(MC)
                    
                    if I[Iv][Yc][Xc] == 0:
                        setFillColor(SC)
                    
                    fill()
                
                
                if getKeyCode() == 32:
                    if St:
                        ht()
                        St = False
                        
                    else:
                        st()
                        St = True
                    
                Xc = Xc + 1
                
            Yc = Yc + 1
                    
        
        setStatusText('Generation: ' + str(Iv) + ' Time: ' + str(t.time()-T) + 's')
        
        if I[Iv] == I[Iv - 1] and Iv > 1:            
            break
       
        B = .5+(T-t.time())
        
        if B < 0:
            B = 0
            
        t.sleep(B)
        

           
def coords(x, y):
    
    if not end:
        setPos(x,y)
        
        if getPixelColorStr() == "white":
            setFillColor("black")
            fill()
            
        elif getPixelColorStr() == "black":
            setFillColor("white")
            fill()
            
    else:
        pass

    
    
def get_started():
    global end    
    end = False
    
    while end==False:
        onMouseClicked(coords)
        
        if getKeyCode() == 10:
              end = True
             
def matrix(Xv, Yv):
    grid_as_matrix = []
    
    for i in range(Yv):
        horizontal_matrix = []
        
        for j in range(Xv):
            horizontal_matrix.append(0)
        
        grid_as_matrix.append(horizontal_matrix)
        
    return(grid_as_matrix)
  
def scan(Xv, Yv):
    
    size = getsize(Xv, Yv)
        
    St = False
    startposition = [-(getPlaygroundWidth() / 2 * .9), -(getPlaygroundHeight() / 2 * .9)]
    setPos(startposition[0]+0.5*size, startposition[1]+(Yv-1)*size+size*0.5)    
    current_y = 0    
    pos = getPos()
    
    repeat Yv:       
        current_x = 0
        
        repeat Xv: 
            setPos(pos[0] + current_x*size, pos[1] - current_y*size)
            
            if getPixelColorStr() == "black":
                I[Iv][current_y][current_x] = 1
                
            else:
                I[Iv][current_y][current_x] = 0
                
            if getKeyCode() == 32:
                    if St:
                        ht()
                        St = False
                        
                    else:
                        st()
                        St = True
                     
            current_x += 1
           
        current_y += 1
        
        setStatusText("|"*current_y*8)
    ht()


spielfeld(Xv, Yv)

get_started()

I = [matrix(Xv, Yv)]

addStatusBar(20)

scan(Xv, Yv)

cs()

gameoflife(I, MI, Xv, Yv)
                