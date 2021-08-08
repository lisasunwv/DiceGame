import graphics 

class Money():
    def __init__(self,win):
        self.money = 100
        self.textMoney = graphics.Text(graphics.Point(50,10),"100")
        self.textMoney.draw(win)
        #self.win = win
    def moneyWon(self, RoleNum):
        moneyWon = 0
        FullHouse = "false"
        duplicates = []
        for i in range(1,7):
            duplicates.append(RoleNum.count(i))

        print(duplicates)
              

        for i in duplicates:
            if i == 2:
                 for j in duplicates:
                     if j == 3:
                          moneyWon = moneyWon + 12
                          FullHouse = "true"
                          
        if FullHouse == "false":                  
            for i in duplicates:
                if i == 5:
                    moneyWon = moneyWon + 30
                    print("30,i=5")
                elif i == 4:
                    moneyWon = moneyWon + 15
                    print("15,i=4")
                elif i == 3:
                    moneyWon = moneyWon + 8
                    print("8,i=3")
                elif i == 2:
                    moneyWon = moneyWon + 5
                    print("5,i=2")

        if FullHouse == "false":
            if(duplicates.count(1) == 5):
                moneyWon = moneyWon + 20
                print("20,i=1")

        print(moneyWon, "added")
        return moneyWon

    def updateMoney(self,money,win):
        self.money = self.money + money
        self.textMoney.setText(self.money)
##        self.textMoney.draw(win)

    def getMon():
        return self.money

        
