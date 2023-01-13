import Treasury
import Furnace
import Mint
import Sawmill

platinumCoin = Treasury.itemSet("coin").copy()
platinumCoin.addAttribute(platinumCoin)
silverCoin = Treasury.itemSet("coin").copy()
silverCoin.addAttribute(silverCoin)
goldCoin = Treasury.itemSet("coin").copy()
goldCoin.addAttribute(goldCoin)
bronzeCoin = Treasury.itemSet("coin").copy()
bronzeCoin.addAttribute(bronzeCoin)
ironCoin = Treasury.itemSet("coin").copy()
ironCoin.addAttribute(ironCoin)
copperCoin = Treasury.itemSet("coin").copy()
copperCoin.addAttribute(copperCoin)
woodenCoin = Treasury.itemSet("coin").copy()
woodenCoin.addAttribute(woodenCoin)

def payUp(amount):
    toPay = amount
    while Treasury.numberItems("platinum coin") > 0 and toPay > platinumCoin.value:
        toPay = toPay - platinumCoin.value
        Treasury.removeItem(platinumCoin)
    while Treasury.numberItems("gold coin") > 0 and toPay > goldCoin.value:
        toPay = toPay - goldCoin.value
        Treasury.removeItem(goldCoin)
    while Treasury.numberItems("silver coin") > 0 and toPay > silverCoin.value:
        toPay = toPay - silverCoin.value
        Treasury.removeItem(silverCoin)
    while Treasury.numberItems("bronze coin") > 0 and toPay > bronzeCoin.value:
        toPay = toPay - bronzeCoin.value
        Treasury.removeItem(bronzeCoin)
    while Treasury.numberItems("iron coin") > 0 and toPay > ironCoin.value:
        toPay = toPay - ironCoin.value
        Treasury.removeItem(ironCoin)
    while Treasury.numberItems("copper coin") > 0 and toPay > copperCoin.value:
        toPay = toPay - copperCoin.value
        Treasury.removeItem(copperCoin)
    while Treasury.numberItems("wooden coin") > 0 and toPay > woodenCoin.value:
        toPay = toPay - woodenCoin.value
        Treasury.removeItem(woodenCoin)


class Miner:

    count = 0
    pay = 2

    def work(self):
        for i in range(self.count):
            payUp(self.pay * self.count)
            Furnace.mineStone()


class Lumberer:

    count = 0
    pay = 2

    def work(self):
        for i in range(self.count):
            payUp(self.pay * self.count)
            Sawmill.gatherWood()
        
class Carpenter:

    count = 0
    pay = 2

    def work(self):
        for i in range(self.count):
            payUp(self.pay * self.count)
            Sawmill.craftPlank()

class metalWorker:

    count = 0
    pay = 3

    def work(self):
        for i in range(self.count):
            payUp(self.pay * self.count)
        

class coinSmith:

    count = 0
    pay = 5

    def work(self):
        for i in range(self.count):
            payUp(self.pay * self.count)
        