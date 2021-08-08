import graphics
import random

class Dice:
    def __init__(self, win, center, width):
        centX = center.getX()
        centY = center.getY()
        self.xmax = centX+width/2
        self.xmin = centX-width/2
        self.ymax = centY+width/2
        self.ymin = centY-width/2
        
        self.rec = graphics.Rectangle(graphics.Point(self.xmin, self.ymin), graphics.Point(self.xmax, self.ymax))
        self.rec.setFill("white")
        self.rec.draw(win)

        self.pip1 = graphics.Circle(graphics.Point(centX,centY),width/11) 
        self.pip2 = graphics.Circle(graphics.Point(centX+(width/4),centY+(width/4)),width/11)
        self.pip3 = graphics.Circle(graphics.Point(centX-(width/4),centY+(width/4)),width/11)
        self.pip4 = graphics.Circle(graphics.Point(centX+(width/4),centY-(width/4)),width/11)
        self.pip5 = graphics.Circle(graphics.Point(centX-(width/4),centY-(width/4)),width/11)
        self.pip6 = graphics.Circle(graphics.Point(centX+(width/4),centY),width/11)
        self.pip7 = graphics.Circle(graphics.Point(centX-(width/4),centY),width/11)

        self.pip1.draw(win)
        self.pip2.draw(win)
        self.pip3.draw(win)
        self.pip4.draw(win)
        self.pip5.draw(win)
        self.pip6.draw(win)
        self.pip7.draw(win)

        self.pip1.setFill("white")
        self.pip1.setOutline("white")
        self.pip2.setFill("white")
        self.pip2.setOutline("white")
        self.pip3.setFill("white")
        self.pip3.setOutline("white")
        self.pip4.setFill("white")
        self.pip4.setOutline("white")
        self.pip5.setFill("white")
        self.pip5.setOutline("white")
        self.pip6.setFill("white")
        self.pip6.setOutline("white")
        self.pip7.setFill("white")
        self.pip7.setOutline("white")
        
    def role(self):
        ranint = random.randrange(1,6)
        return ranint
    
    def diceDisplay(self,num):
        if num == 1:
            self.pip1.setFill("black")
            self.pip1.setOutline("black")
            
        elif num == 2:
            self.pip7.setFill("black")
            self.pip7.setOutline("black")
            self.pip6.setFill("black")
            self.pip6.setOutline("black")
            
        elif num == 3:
            self.pip3.setFill("black")
            self.pip3.setOutline("black")
            self.pip1.setFill("black")
            self.pip1.setOutline("black")
            self.pip4.setFill("black")
            self.pip4.setOutline("black")
            
        elif num == 4:
            self.pip2.setFill("black")
            self.pip2.setOutline("black")
            self.pip3.setFill("black")
            self.pip3.setOutline("black")
            self.pip4.setFill("black")
            self.pip4.setOutline("black")
            self.pip5.setFill("black")
            self.pip5.setOutline("black")

        elif num == 5:
            self.pip2.setFill("black")
            self.pip2.setOutline("black")
            self.pip3.setFill("black")
            self.pip3.setOutline("black")
            self.pip4.setFill("black")
            self.pip4.setOutline("black")
            self.pip5.setFill("black")
            self.pip5.setOutline("black")
            self.pip1.setFill("black")
            self.pip1.setOutline("black")

        elif num == 6:
            self.pip2.setFill("black")
            self.pip2.setOutline("black")
            self.pip3.setFill("black")
            self.pip3.setOutline("black")
            self.pip4.setFill("black")
            self.pip4.setOutline("black")
            self.pip5.setFill("black")
            self.pip5.setOutline("black")
            self.pip6.setFill("black")
            self.pip6.setOutline("black")
            self.pip7.setFill("black")
            self.pip7.setOutline("black")
           
    def diceClear(self):
        self.pip1.setFill("white")
        self.pip1.setOutline("white")
        self.pip2.setFill("white")
        self.pip2.setOutline("white")
        self.pip3.setFill("white")
        self.pip3.setOutline("white")
        self.pip4.setFill("white")
        self.pip4.setOutline("white")
        self.pip5.setFill("white")
        self.pip5.setOutline("white")
        self.pip6.setFill("white")
        self.pip6.setOutline("white")
        self.pip7.setFill("white")
        self.pip7.setOutline("white")        
