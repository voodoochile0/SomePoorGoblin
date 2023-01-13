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

Treasury.generateStartingStash()

def update_game():
    sawmillLabel.config(text="Sawmill Level " + str(Sawmill.level) + "\n" + Sawmill.buildReqsStr())
    mintLabel.config(text="Mint Level " + str(Mint.level) + "\n" + Mint.buildReqsStr())
    furnaceLabel.config(text="Furnace Level " + str(Furnace.level) + "\n" + Furnace.buildReqsStr())
    treasuryLabel.configure(text=Treasury.stringify())
    freeWorkersLabel.configure(text="Unemployed Goblins: " + str(Goblins.unemployed))
    lumbererLabel.configure(text="Lumberers: \n" + str(Goblins.Lumberer.count))

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
treasuryLabel.grid(column=0, row=0, rowspan=8, sticky='N', pady=16)

chopWoodButton = tk.Button(text="Chop Wood", command=lambda: [Sawmill.gatherWood(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
chopWoodButton.grid(column=1,row=0)

mineStone = tk.Button(text="Mine Stone", command=lambda: [Furnace.mineStone(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
mineStone.grid(column=1,row=1)


sawmillLabel = tk.Label(text="Sawmill Level " + str(Sawmill.level) + "\n" + Sawmill.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT * 2)
sawmillLabel.grid(column=2,row=0)
upgradeSawmillButton = tk.Button(text="Upgrade Sawmill", command=lambda: [Sawmill.upgrade(Sawmill), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeSawmillButton.grid(column=2,row=1)

craftPlankButton = tk.Button(text="Craft Plank", command=lambda: [Sawmill.craftPlank(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlankButton.grid(column=2,row=2)


mintLabel = tk.Label(text="Mint Level " + str(Mint.level) + "\n" + Mint.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT * 2)
mintLabel.grid(column=3,row=0)
upgradeMintButton = tk.Button(text="Upgrade Mint", command=lambda: [Mint.upgrade(Mint), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeMintButton.grid(column=3,row=1)

craftCopperCoinButton = tk.Button(text="Craft Copper Coin", command=lambda: [Mint.mintCoins("copper"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftCopperCoinButton.grid(column=3,row=2)

craftIronCoinButton = tk.Button(text="Craft Iron Coin", command=lambda: [Mint.mintCoins("iron"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftIronCoinButton.grid(column=3,row=3)

craftBronzeCoinButton = tk.Button(text="Craft Bronze Coin", command=lambda: [Mint.mintCoins("bronze"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftBronzeCoinButton.grid(column=3,row=4)

craftSilverCoinButton = tk.Button(text="Craft Silver Coin", command=lambda: [Mint.mintCoins("silver"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftSilverCoinButton.grid(column=3,row=5)

craftGoldCoinButton = tk.Button(text="Craft Gold Coin", command=lambda: [Mint.mintCoins("gold"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftGoldCoinButton.grid(column=3,row=6)

craftPlatinumCoinButton = tk.Button(text="Craft Platinum Coin", command=lambda: [Mint.mintCoins("platinum"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlatinumCoinButton.grid(column=3,row=7)

coinButtons = [craftCopperCoinButton, craftIronCoinButton, craftBronzeCoinButton, craftSilverCoinButton, craftGoldCoinButton, craftPlatinumCoinButton]

furnaceLabel = tk.Label(text="Furnace Level " + str(Furnace.level) + "\n" + Furnace.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT * 2)
furnaceLabel.grid(column=4,row=0)
upgradeFurnaceButton = tk.Button(text="Upgrade Furnace", command=lambda: [Furnace.upgrade(Furnace), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeFurnaceButton.grid(column=4,row=1)

craftCopperBarButton = tk.Button(text="Craft Copper Bar", command=lambda: [Furnace.smeltBar("copper"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftCopperBarButton.grid(column=4,row=3)

craftIronBarButton = tk.Button(text="Craft Iron Bar", command=lambda: [Furnace.smeltBar("iron"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftIronBarButton.grid(column=4,row=4)

craftBronzeBarButton = tk.Button(text="Craft Bronze Bar", command=lambda: [Furnace.smeltBar("bronze"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftBronzeBarButton.grid(column=4,row=5)

craftSilverBarButton = tk.Button(text="Craft Silver Bar", command=lambda: [Furnace.smeltBar("silver"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftSilverBarButton.grid(column=4,row=6)

craftGoldBarButton = tk.Button(text="Craft Gold Bar", command=lambda: [Furnace.smeltBar("gold"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftGoldBarButton.grid(column=4,row=7)

craftPlatinumBarButton = tk.Button(text="Craft Platinum Bar", command=lambda: [Furnace.smeltBar("platinum"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlatinumBarButton.grid(column=4,row=8)

barButtons = [craftCopperBarButton, craftIronBarButton, craftBronzeBarButton, craftSilverBarButton, craftGoldBarButton, craftPlatinumBarButton]

freeWorkersLabel = tk.Label(text="Unemployed Goblins:" + str(Goblins.unemployed))
freeWorkersLabel.grid(column=1,row=2)

removeLumbererButton = tk.Button(text="-", command=lambda: [Goblins.removeLumberer(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)
lumbererLabel = tk.Label(text="Lumberers: \n" + str(Goblins.Lumberer.count), width=int(GRIDWIDTH / 2))
addLumbererButton = tk.Button(text="+", command=lambda: [Goblins.addLumberer(), update_game()], width=int(GRIDWIDTH / 5), height=GRIDHEIGHT)

removeLumbererButton.grid(column = 1, row = 3, sticky='W',pady=4)
lumbererLabel.grid(column=1,row=3)
addLumbererButton.grid(column=1,row=3,sticky='E')



checkButtons()

game.mainloop()