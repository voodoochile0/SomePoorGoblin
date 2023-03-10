import Treasury
import Furnace
import Mint
import Sawmill

platinumCoin = Treasury.itemSet["coin"].copy()
platinumCoin.addAttribute("platinum")
silverCoin = Treasury.itemSet["coin"].copy()
silverCoin.addAttribute("silver")
goldCoin = Treasury.itemSet["coin"].copy()
goldCoin.addAttribute("gold")
bronzeCoin = Treasury.itemSet["coin"].copy()
bronzeCoin.addAttribute("bronze")
ironCoin = Treasury.itemSet["coin"].copy()
ironCoin.addAttribute("iron")
copperCoin = Treasury.itemSet["coin"].copy()
copperCoin.addAttribute("copper")

global unemployed
unemployed = 0

valueThreshold = 100

types = ["copper", "iron", "bronze", "silver", "gold", "platinum"]
types.reverse()

def payUp(amount):
    toPay = amount

    while Treasury.numberItems("platinum coin") > 0 and toPay > platinumCoin.value:
        toPay = toPay - platinumCoin.value
        Treasury.removeItem("platinum coin")
    while Treasury.numberItems("gold coin") > 0 and toPay > goldCoin.value:
        toPay = toPay - goldCoin.value
        Treasury.removeItem("gold coin")
    while Treasury.numberItems("silver coin") > 0 and toPay > silverCoin.value:
        toPay = toPay - silverCoin.value
        Treasury.removeItem("silver coin")
    while Treasury.numberItems("bronze coin") > 0 and toPay > bronzeCoin.value:
        toPay = toPay - bronzeCoin.value
        Treasury.removeItem("bronze coin")
    while Treasury.numberItems("iron coin") > 0 and toPay > ironCoin.value:
        toPay = toPay - ironCoin.value
        Treasury.removeItem("iron coin")
    while Treasury.numberItems("copper coin") > 0 and toPay > 0:
        toPay = toPay - copperCoin.value
        Treasury.removeItem("copper coin")

    while Treasury.numberItems("iron coin") > 0 and toPay > 0:
        toPay = toPay - ironCoin.value
        Treasury.removeItem("iron coin")
    while Treasury.numberItems("bronze coin") > 0 and toPay > 0:
        toPay = toPay - bronzeCoin.value
        Treasury.removeItem("bronze coin")
    while Treasury.numberItems("silver coin") > 0 and toPay > 0:
        toPay = toPay - silverCoin.value
        Treasury.removeItem("silver coin")
    while Treasury.numberItems("gold coin") > 0 and toPay > 0:
        toPay = toPay - goldCoin.value
        Treasury.removeItem("gold coin")
    while Treasury.numberItems("platinum coin") > 0 and toPay > 0:
        toPay = toPay - platinumCoin.value
        Treasury.removeItem("platinum coin")

    if toPay > 0:
        return False
    return True


class Miner:

    count = 0
    pay = 1

    def work(self):
        if(payUp(self.pay * self.count)):
            for i in range(self.count):
                Furnace.mineStone()

def addMiner():
    global unemployed
    if(unemployed > 0):
        unemployed = unemployed - 1
        Miner.count += 1

def removeMiner():
    global unemployed
    if(Miner.count > 0):
        unemployed = unemployed + 1
        Miner.count -= 1

class Lumberer:

    count = 0
    pay = 1

    def work(self):
        if(payUp(self.pay * self.count)):
            for i in range(self.count):
                Sawmill.gatherWood
        
def addLumberer():
    global unemployed
    if(unemployed > 0):
        unemployed = unemployed - 1
        Lumberer.count += 1

def removeLumberer():
    global unemployed
    if(Lumberer.count > 0):
        unemployed = unemployed + 1
        Lumberer.count -= 1

class Carpenter:

    count = 0
    pay = 1

    def work(self):
        if(payUp(self.pay * self.count)):
            for i in range(self.count):
                Sawmill.craftPlank()

def addCarpenter():
    global unemployed
    if(unemployed > 0):
        unemployed = unemployed - 1
        Carpenter.count += 1

def removeCarpenter():
    global unemployed
    if(Carpenter.count > 0):
        unemployed = unemployed + 1
        Carpenter.count -= 1

class metalWorker:
    
    count = 0
    pay = 2

    def work(self):
        if(payUp(self.pay * self.count)):
            for i in range(self.count):
                for i in range(len(types)):
                    if(Furnace.canSmeltBar(types[i])):
                        Furnace.smeltBar(types[i])
                        return

def addMetalWorker():
    global unemployed
    if(unemployed > 0):
        unemployed = unemployed - 1
        metalWorker.count += 1

def removeMetalWorker():
    global unemployed
    if(metalWorker.count > 0):
        unemployed = unemployed + 1
        metalWorker.count -= 1

class coinSmith:

    count = 0
    pay = 3

    def work(self):
        if(payUp(self.pay * self.count)):
            for i in range(self.count):
                for i in range(len(types)):
                    if(Mint.canCraft(types[i])):
                        Mint.canCraft(types[i])
                        return

def addCoinSmith():
    global unemployed
    if(unemployed > 0):
        unemployed = unemployed - 1
        coinSmith.count += 1

def removeCoinSmith():
    global unemployed
    if(coinSmith.count > 0):
        unemployed = unemployed + 1
        coinSmith.count -= 1

def addGoblins(self, num):
    self.unemployed = self.unemployed + num

def updateGoblins(self):

    if(Treasury.totalValue() > valueThreshold):
        addGoblins(self, 5)
        self.valueThreshold = self.valueThreshold * 1.5
    
    for i in range(Miner.count):
        Miner.work(Miner)

    for i in range(Lumberer.count):
        Lumberer.work(Lumberer)

    for i in range(Carpenter.count):
        Carpenter.work(Carpenter)

    for i in range(metalWorker.count):
        metalWorker.work(metalWorker)

    for i in range(coinSmith.count):
        coinSmith.work(coinSmith)
