from gturtle import * 
import time as t            #time wird benötigt um einfach die zeit zu messen
import random as r

Speed = 1000        #Die Geschwindigkeit der Schildkröte
TurtleColor = 'green'    #Die Farbe der Schildkröte
PenColor = 'grey'     #Die Farbe des Grids
SnakeColor = 'black'    #Die Farbe aktiver Felder
BoardColor = 'white'    #Die Farbe inaktiver Felder
HideTurtle = False      #HideTurtle an oder aus (versteckt die Schildkröte und alles wird sofort gezeichnet)
Width = inputInt("Breite des Spielfeldes in Quadraten: ")      #Die Breite des Spielfelds in Feldern
Height = inputInt("Höhe des Spielfeldes in Quadraten: ")        #Die Höhe des SpielFelds in Feldern
X_current = 0      #Die actuelle X iteration in einer funktion
Y_current = 0      #Die actuelle Y iteration in einer funktion
Points = 0      #Dieaktuelle Länge der Snake

x, y = getScreenSize()  #Die X und Y Größe des Turtle Fensters in pixeln
x /= 1.15    #Die X-Ausdehnung des Turtlefensters wird festgelegt (Je näher der Dividend an 1 ist desto größer ist das Turtlefenster)
y /= 1.15    #Die Y-Ausdehnung des Turtlefensters wird festgelegt (Je näher der Dividend an 1 ist desto größer ist das Turtlefenster)

makeTurtle()    #Die Turtle wird erzeugt
ht()            #Die Turtle wird versteckt
setPenColor(PenColor) #Die Stifftfarbe wird festgesetzt

setPlaygroundSize(int(x), int(y))   #Die Spielfeldgröße wird anhand der vorher ermittelten Werte festgelegt

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
    


class Player:
    
    def __init__(self, Height, Width):
        
        self.Points = -1
        
        self.draw_start = [-0.9*getPlaygroundWidth()/2, -0.9*getPlaygroundHeight()/2]
        self.size = getsize(Width, Height)
        
        self.SnakeColor = SnakeColor
          
        self.Heading = 0
        
        self.All_pos = []
        
        self.Apples = []
        
        apple_number = 0
        
        self.X_current = 20
        self.Y_current = int(Height/2)
        
        self.X_last = self.X_current-1
        self.Y_last = self.Y_current
        
        self.Heading = 2
        
        for P in range(5):
            print(P)
            self.add_point(P)
            
        
        
    def data_refresh(self):
        
        self.check_keyboard_input()
        
        self.X_last = self.X_current
        self.Y_last = self.Y_current
        
        if self.Heading == 1:
            self.Y_current += 1
            
        if self.Heading == 2:
            self.X_current -= 1
            
        if self.Heading == 3:
            self.Y_current -= 1
        
        if self.Heading == 4:
            self.X_current += 1
            
            
        for i in list(self.All_pos):
            print(i.pos_in_snake)
            if i.pos_in_snake == 0:
                self.All_pos[0].X_last = self.All_pos[0].X_current
                self.All_pos[0].Y_last = self.All_pos[0].Y_current
                
                self.All_pos[0].X_current = self.X_last
                self.All_pos[0].Y_current = self.Y_last
                
            else:
                
                i.X_last = i.X_current
                i.Y_last = i.Y_current
                
                i.X_current = self.All_pos[i.pos_in_snake-1].X_last
                i.Y_current = self.All_pos[i.pos_in_snake-1].Y_last
                
    
    
    def add_apple():
        Apples.append(Apple(r.randomInt(0, width), r.randomInt(0, Height), apple_number, self))
        apple_number += 1
                
    
    def draw_snake(self):
        setPos(self.draw_start[0]+self.X_current*self.size+.5*self.size, self.draw_start[1]+self.Y_current*self.size+.5*self.size)
        setFillColor(self.SnakeColor)
        fill()
        
        for d in self.All_pos:
            
            setPos(self.draw_start[0]+d.X_current*self.size+.5*self.size, self.draw_start[1]+d.Y_current*self.size+.5*self.size)
            
            setFillColor(self.SnakeColor)
            fill()
            
            #print(str(d.pos_in_snake) + ' ' + str(self.Points))
            
            print(str(d.X_current) + str(d.Y_current))
            
            if d.pos_in_snake == self.Points:
                
                setPos(self.draw_start[0]+d.X_last*self.size+.5*self.size, self.draw_start[1]+d.Y_last*self.size+.5*self.size)
                
                setFillColor(BoardColor)
                fill()
                
            
    def check_boundaries(self):
        if self.X_current < 0 or self.X_current > Width - 1:
            return(True)
        elif self.Y_current < 0 or self.Y_current > Height - 1:
            return(True)
        
    def check_keyboard_input(self):
        
        G = getKeyCode()
        
        if G == 87:# or getKeyCode() == 119:
            
            print('W')
            
            self.Heading = 1
            
        elif G == 65:# or getKeyCode() == 97:
            
            print('A')
            
            self.Heading = 2
            
        elif G == 83:# or getKeyCode() == 115:
            
            print('S')
            
            self.Heading = 3
            
        elif G == 68:# or getKeyCode() == 100:
            
            print('D')
            
            self.Heading = 4
            
        #else:
         #   print('?')
            
        #if getKeyCode() == 87:
            
            #print('W')
            
            #self.Heading = 1
        
        
    def check_snake_collision(self):
        
        for i in self.All_pos:
            if i.X_current == self.X_current and i.Y_current == self.Y_current:
                return(True)
    
    
    
    def add_point(self, P):
        self.Points += 1
        self.All_pos.append(snake_segment(self, P))
    
        
    

class snake_segment:
    
    def __init__(self, Snake, pos):
        
        self.Last = True
        
        self.pos_in_snake = pos
        self.Snake = Snake
        
        if pos > 0:
            self.X_current = self.Snake.All_pos[pos-1].X_last
            self.Y_current = self.Snake.All_pos[pos-1].Y_last
            
        else:
            self.X_current = self.Snake.X_last
            self.Y_current = self.Snake.Y_last
        
        self.X_last = 0
        self.Y_last = 0 
        
        
    
    

class Apple():
    def __init__(self, X_pos, Y_pos, count, snake):
        self.X_pos = X_pos
        self.Y_pos = Y_pos
        self.count = count
        self.snake = snake
        
        setPos(self.snake.draw_start[0]+self.snake.size*)
    
    def get_eaten(self, snake):
        snake.add_point(snake.Point)
        
    
    
        

spielfeld(Width, Height)
    
x = Player(Height, Width)
god_mode = True
    
while True:
    x.data_refresh()
    if x.check_boundaries() or x.check_snake_collision() and god_mode == False:
        break
    x.draw_snake()
    t.sleep(.5)
    god_mode = False
    
addStatusBar(20)
setStatusText('Du hast verloren, dein Punktestand beträgt: ' + str(x.Points - 4))