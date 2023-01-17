from time import sleep
import time
import Treasury
import Sawmill
import tkinter as tk
import Furnace
import Mint
import Goblins

attributeSet = {}
ITEMFILE = "data/items.txt"
ATTRFILE = "data/attributes.txt"

GRIDWIDTH = 20
GRIDHEIGHT = 3

TRESCOL = 0
GOBCOL = 1
SAWCOL = 2
MINTCOL = 3
MINTCOL = 4
FURCOL = 5

## COLORS: d = dark, l = light, b = brown, g = green
ddb = "#582F0E"
db = "#7F4F24"
b = "#936639"
lb = "#A68A64"
llb = "#B6AD90"
llg = "#C2C5AA"
lg = "#A4AC86"
g = "#656D4A"
dg = "#414833"
ddg = "#333D29"

Treasury.generateStartingStash()

def update_game():

    sawmillLabel.config(text="Sawmill Level " + str(Sawmill.level) + "\n" + Sawmill.buildReqsStr())
    mintLabel.config(text="Mint Level " + str(Mint.level) + "\n" + Mint.buildReqsStr())
    furnaceLabel.config(text="Furnace Level " + str(Furnace.level) + "\n" + Furnace.buildReqsStr())
    treasuryLabel.configure(text=Treasury.stringify())

    freeWorkersLabel.configure(text="Unemployed Goblins: " + str(Goblins.unemployed))
    lumbererLabel.configure(text="Lumberers: \n" + str(Goblins.Lumberer.count) + "\nWage: " + str(Goblins.Lumberer.count * Goblins.Lumberer.pay))
    carpenterLabel.configure(text="Carpenters: \n" + str(Goblins.Carpenter.count) + "\nWage: " + str(Goblins.Carpenter.count * Goblins.Carpenter.pay))
    minerLabel.configure(text="Miners: \n" + str(Goblins.Miner.count) + "\nWage: " + str(Goblins.Miner.count * Goblins.Miner.pay))
    coinsmithLabel.configure(text="CoinSmiths: \n" + str(Goblins.coinSmith.count) + "\nWage: " + str(Goblins.coinSmith.count * Goblins.coinSmith.pay))
    metalworkerLabel.configure(text="MetalWorkers: \n" + str(Goblins.metalWorker.count) + "\nWage: " + str(Goblins.metalWorker.count * Goblins.metalWorker.pay))

    checkButtons()
    Goblins.updateGoblins(Goblins)

def handle_click(event):
    update_game()

def checkButtons():

    if(Sawmill.canUpgrade()):
        upgradeSawmillButton.grid()
    else:
        upgradeSawmillButton.grid_remove()
    if(Sawmill.canCraftPlank()):
        craftPlankButton.grid()
    else:
        craftPlankButton.grid_remove()
    
    if(Mint.canUpgrade()):
        upgradeMintButton.grid()
    else:
        upgradeMintButton.grid_remove()

    for i in range(len(coinButtons)):
        if Mint.canCraft(types[i]):
            coinButtons[i].grid()
        else:
            coinButtons[i].grid_remove()

    if(Furnace.canUpgrade()):
        upgradeFurnaceButton.grid()
    else:
        upgradeFurnaceButton.grid_remove()

    for i in range(len(barButtons)):
        if Furnace.canSmeltBar(types[i]):
            barButtons[i].grid()
        else:
            barButtons[i].grid_remove()

game = tk.Tk()

types = ["copper", "iron", "bronze", "silver", "gold", "platinum"]

treasuryLabel = tk.Label(text=Treasury.stringify(), width=GRIDWIDTH)
treasuryLabel.grid(column=TRESCOL, row=0, rowspan=8, sticky='E', pady=16)

chopWoodButton = tk.Button(text="Chop Wood", command=lambda: [Sawmill.gatherWood(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
chopWoodButton.grid(column=GOBCOL,row=0)

mineStone = tk.Button(text="Mine Stone", command=lambda: [Furnace.mineStone(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
mineStone.grid(column=GOBCOL,row=1)


sawmillLabel = tk.Label(text="Sawmill Level " + str(Sawmill.level) + "\n" + Sawmill.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT * 2)
sawmillLabel.grid(column=SAWCOL,row=0)
upgradeSawmillButton = tk.Button(text="Upgrade Sawmill", command=lambda: [Sawmill.upgrade(Sawmill), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeSawmillButton.grid(column=SAWCOL,row=1)

craftPlankButton = tk.Button(text="Craft Plank", command=lambda: [Sawmill.craftPlank(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlankButton.grid(column=SAWCOL,row=2)

## MINT ##
mintLabel = tk.Label(text="Mint Level " + str(Mint.level) + "\n" + Mint.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT * 2)
mintLabel.grid(column=MINTCOL,row=0)
upgradeMintButton = tk.Button(text="Upgrade Mint", command=lambda: [Mint.upgrade(Mint), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeMintButton.grid(column=MINTCOL,row=1)

craftCopperCoinButton = tk.Button(text="Craft Copper Coin", command=lambda: [Mint.mintCoins("copper"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftCopperCoinButton.grid(column=MINTCOL,row=2)

craftIronCoinButton = tk.Button(text="Craft Iron Coin", command=lambda: [Mint.mintCoins("iron"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftIronCoinButton.grid(column=MINTCOL,row=3)

craftBronzeCoinButton = tk.Button(text="Craft Bronze Coin", command=lambda: [Mint.mintCoins("bronze"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftBronzeCoinButton.grid(column=MINTCOL,row=4)

craftSilverCoinButton = tk.Button(text="Craft Silver Coin", command=lambda: [Mint.mintCoins("silver"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftSilverCoinButton.grid(column=MINTCOL,row=5)

craftGoldCoinButton = tk.Button(text="Craft Gold Coin", command=lambda: [Mint.mintCoins("gold"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftGoldCoinButton.grid(column=MINTCOL,row=6)

craftPlatinumCoinButton = tk.Button(text="Craft Platinum Coin", command=lambda: [Mint.mintCoins("platinum"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlatinumCoinButton.grid(column=MINTCOL,row=7)

coinButtons = [craftCopperCoinButton, craftIronCoinButton, craftBronzeCoinButton, craftSilverCoinButton, craftGoldCoinButton, craftPlatinumCoinButton]

## FURNACE ##
furnaceLabel = tk.Label(text="Furnace Level " + str(Furnace.level) + "\n" + Furnace.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT * 2)
furnaceLabel.grid(column=FURCOL,row=0)
upgradeFurnaceButton = tk.Button(text="Upgrade Furnace", command=lambda: [Furnace.upgrade(Furnace), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeFurnaceButton.grid(column=FURCOL,row=1)

craftCopperBarButton = tk.Button(text="Craft Copper Bar", command=lambda: [Furnace.smeltBar("copper"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftCopperBarButton.grid(column=FURCOL,row=3)

craftIronBarButton = tk.Button(text="Craft Iron Bar", command=lambda: [Furnace.smeltBar("iron"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftIronBarButton.grid(column=FURCOL,row=4)

craftBronzeBarButton = tk.Button(text="Craft Bronze Bar", command=lambda: [Furnace.smeltBar("bronze"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftBronzeBarButton.grid(column=FURCOL,row=5)

craftSilverBarButton = tk.Button(text="Craft Silver Bar", command=lambda: [Furnace.smeltBar("silver"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftSilverBarButton.grid(column=FURCOL,row=6)

craftGoldBarButton = tk.Button(text="Craft Gold Bar", command=lambda: [Furnace.smeltBar("gold"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftGoldBarButton.grid(column=FURCOL,row=7)

craftPlatinumBarButton = tk.Button(text="Craft Platinum Bar", command=lambda: [Furnace.smeltBar("platinum"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlatinumBarButton.grid(column=FURCOL,row=8)

barButtons = [craftCopperBarButton, craftIronBarButton, craftBronzeBarButton, craftSilverBarButton, craftGoldBarButton, craftPlatinumBarButton]

## WORKERS ##

freeWorkersLabel = tk.Label(text="Unemployed Goblins:" + str(Goblins.unemployed))
freeWorkersLabel.grid(column=GOBCOL,row=2)

## LUMBERER GOBLINS
removeLumbererButton = tk.Button(text="-", command=lambda: [Goblins.removeLumberer(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)
lumbererLabel = tk.Label(text="Lumberers: \n" + str(Goblins.Lumberer.count) + "\nWage: " + str(Goblins.Lumberer.count * Goblins.Lumberer.pay), width=int(GRIDWIDTH / 2))
addLumbererButton = tk.Button(text="+", command=lambda: [Goblins.addLumberer(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)

removeLumbererButton.grid(column = GOBCOL, row = 3, sticky='W',pady=4)
lumbererLabel.grid(column=GOBCOL,row=3)
addLumbererButton.grid(column=GOBCOL,row=3,sticky='E')

## CARPENTER GOBLINS
removeCarpenterButton = tk.Button(text="-", command=lambda: [Goblins.removeCarpenter(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)
carpenterLabel = tk.Label(text="Carpenters: \n" + str(Goblins.Carpenter.count) + "\nWage: " + str(Goblins.Carpenter.count * Goblins.Carpenter.pay), width=int(GRIDWIDTH / 2))
addCarpenterButton = tk.Button(text="+", command=lambda: [Goblins.addCarpenter(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)

removeCarpenterButton.grid(column = GOBCOL, row = 4, sticky='W',pady=4)
carpenterLabel.grid(column=GOBCOL,row=4)
addCarpenterButton.grid(column=GOBCOL,row=4,sticky='E')

## MINER GOBLINS
removeMinerButton = tk.Button(text="-", command=lambda: [Goblins.removeMiner(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)
minerLabel = tk.Label(text="Miners: \n" + str(Goblins.Miner.count) + "\nWage: " + str(Goblins.Miner.count * Goblins.Miner.pay), width=int(GRIDWIDTH / 2))
addMinerButton = tk.Button(text="+", command=lambda: [Goblins.addMiner(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)

removeMinerButton.grid(column = GOBCOL, row = 5, sticky='W',pady=4)
minerLabel.grid(column=GOBCOL,row=5)
addMinerButton.grid(column=GOBCOL,row=5,sticky='E')

## COINSMITH GOBLINS
removeCoinSmithButton = tk.Button(text="-", command=lambda: [Goblins.removeCoinSmith(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)
coinsmithLabel = tk.Label(text="CoinSmiths: \n" + str(Goblins.coinSmith.count) + "\nWage: " + str(Goblins.coinSmith.count * Goblins.coinSmith.pay), width=int(GRIDWIDTH / 2))
addCoinSmithButton = tk.Button(text="+", command=lambda: [Goblins.addCoinSmith(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)

removeCoinSmithButton.grid(column = GOBCOL, row = 6, sticky='W',pady=4)
coinsmithLabel.grid(column=GOBCOL,row=6)
addCoinSmithButton.grid(column=GOBCOL,row=6,sticky='E')

## METALWORKER GOBLINS
removeMetalWorkerButton = tk.Button(text="-", command=lambda: [Goblins.removeMetalWorker(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)
metalworkerLabel = tk.Label(text="MetalWorkers: \n" + str(Goblins.metalWorker.count) + "\nWage: " + str(Goblins.metalWorker.count * Goblins.metalWorker.pay), width=int(GRIDWIDTH / 2))
addMetalWorkerButton = tk.Button(text="+", command=lambda: [Goblins.addMetalWorker(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)

removeMetalWorkerButton.grid(column = GOBCOL, row = 7, sticky='W',pady=4)
metalworkerLabel.grid(column=GOBCOL,row=7)
addMetalWorkerButton.grid(column=GOBCOL,row=7,sticky='E')

checkButtons()

game.mainloop()