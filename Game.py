from Button import Button
from Dice import Dice
from Money import Money
import graphics

class Game:
    
    def __init__(self):
        self.win = graphics.GraphWin("Poker",600,600)
        self.win.setCoords(0.0,0.0,100,100)
        self.win.setBackground("pink")
        self.myButtons = []
        #self.diceValues = []
        self.roleNum = []
        
        dice1 = Dice(self.win, graphics.Point(16,80), 10)
        dice2 = Dice(self.win, graphics.Point(33,80), 10)
        dice3 = Dice(self.win, graphics.Point(50,80), 10)
        dice4 = Dice(self.win, graphics.Point(67,80), 10)
        dice5 = Dice(self.win, graphics.Point(84,80), 10)
        self.myDice = [dice1,dice2,dice3,dice4,dice5]

        buttonMappingTable = [[16,65,"Die 1"],[33,65,"Die 2"],[50,65,"Die 3"],
                             [67,65,"Die 4"],[84,65,"Die 5"]]
        for butt in buttonMappingTable:
            self.myButtons.append(Button(self.win,graphics.Point(butt[0],butt[1]),10,5,butt[2]))
            
        self.RoleButt = Button(self.win,graphics.Point(50,50),30,10,"Roll Dice")
        self.ScoreButt = Button(self.win,graphics.Point(50,30),20,10,"Score")
        self.QuitButt = Button(self.win,graphics.Point(90,10),10,5,"Quit")

        self.QuitButt.activate()
        self.RoleButt.activate()

        self.textBox1 = graphics.Text(graphics.Point(50,95),"Python Poker Parlor")
        

    def getDice(self):
        return self.myDice
    
    def getButton(self):
        return self.myButtons

    def getRoleNum(self):
        return self.roleNum

    def roleAll(self):
        self.roleNum = []
        for dice in self.myDice:
            dice.diceClear()
            num = dice.role()
            self.roleNum.append(num)
            dice.diceDisplay(num)
        print(self.roleNum, "rA")

    def inhance(self,button):
        num = 0
        indexOfButton = self.myButtons.index(button)
##        for i in range(4):
##            print (i,"i")
##            if self.myButtons[i] == button:
##                num = i
##                print(i, "ii")
    
        change = self.myDice[indexOfButton]
        newRole = change.role()
        change.diceClear()
        change.diceDisplay(newRole)
        self.roleNum[indexOfButton] = newRole

    def play(self):
        inhan = 0
        value = 0
        Mon = Money(self.win)
        monHave = 0
        notQuit = "true"
        p = self.win.getMouse()
        while notQuit == "true":
            if(self.RoleButt.clicked(p)):
                Mon.updateMoney(-10,self.win)
                self.roleAll()
                self.RoleButt.deactivate()
                self.ScoreButt.activate()
                inhan = 0
                for but in self.myButtons:
                    but.activate() 
                p = self.win.getMouse()
               
            elif (self.QuitButt.clicked(p)):
                notQuit = "false"

            elif(inhan < 2 and (self.myButtons[0].clicked(p) or self.myButtons[1].clicked(p)
                                or self.myButtons[2].clicked(p) or self.myButtons[3].clicked(p) or self.myButtons[4].clicked(p))):
                #print(self.myButtons, "myB")
                for but in self.myButtons:
                    if but.clicked(p):   
                        self.inhance(but)
                        inhan = inhan + 1
                        print(inhan, "inhan")
                        if inhan == 2:
                            for but in self.myButtons:
                                but.deactivate()
                p = self.win.getMouse()

            elif self.ScoreButt.clicked(p):
                value = Mon.moneyWon(self.roleNum)
                Mon.updateMoney(value,self.win)
                for but in self.myButtons:
                    but.deactivate()

                self.ScoreButt.deactivate()
                self.RoleButt.activate()
                for n in self.roleNum:
                    n = ""
                    

            else:
                p = self.win.getMouse()
                 
        self.win.close()           



               
                
