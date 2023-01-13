from time import sleep
import time
import Treasury
import Sawmill
import tkinter as tk
import Furnace
import Mint

attributeSet = {}
ITEMFILE = "data/items.txt"
ATTRFILE = "data/attributes.txt"

GRIDWIDTH = 20
GRIDHEIGHT = 3

Treasury.generateStartingStash()

def update_game():
    treasuryLabel.configure(text=Treasury.stringify())
    checkButtons()

def handle_click(event):
    update_game()

def checkButtons():

    sawmillLabel.config(text="Sawmill Level " + str(Sawmill.level) + "\n" + Sawmill.buildReqsStr())
    mintLabel.config(text="Mint Level " + str(Mint.level) + "\n" + Mint.buildReqsStr())
    furnaceLabel.config(text="Furnace Level " + str(Furnace.level) + "\n" + Furnace.buildReqsStr())

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
        if Mint.canCraft(type[i]):
            coinButtons[i].grid()
        else:
            coinButtons[i].grid_remove()

    if(Furnace.canUpgrade()):
        upgradeFurnaceButton.grid()
    else:
        upgradeFurnaceButton.grid_remove()

    for i in range(len(barButtons)):
        if Furnace.canSmeltBar(type[i+1]):
            barButtons[i].grid()
        else:
            barButtons[i].grid_remove()

    

game = tk.Tk()

types = ["wooden", "copper", "iron", "bronze", "silver", "gold", "platinum"]

treasuryLabel = tk.Label(text=Treasury.stringify())
treasuryLabel.grid(column=0,row=2)

chopWoodButton = tk.Button(text="Chop Wood", command=lambda: [Sawmill.gatherWood(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
chopWoodButton.grid(column=0,row=0)

mineStone = tk.Button(text="Mine Stone", command=lambda: [Furnace.mineStone(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
mineStone.grid(column=0,row=1)


sawmillLabel = tk.Label(text="Sawmill Level " + str(Sawmill.level) + "\n" + Sawmill.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT * 2)
sawmillLabel.grid(column=1,row=0)
upgradeSawmillButton = tk.Button(text="Upgrade Sawmill", command=lambda: [Sawmill.upgrade(Sawmill), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeSawmillButton.grid(column=1,row=1)

craftPlankButton = tk.Button(text="Craft Plank", command=lambda: [Sawmill.craftPlank(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlankButton.grid(column=1,row=2)


mintLabel = tk.Label(text="Mint Level " + str(Mint.level) + "\n" + Mint.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT * 2)
mintLabel.grid(column=2,row=0)
upgradeMintButton = tk.Button(text="Upgrade Mint", command=lambda: [Mint.upgrade(Mint), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeMintButton.grid(column=2,row=1)

craftWoodenCoinButton = tk.Button(text="Craft Wooden Coin", command=lambda: [Mint.mintCoins("wooden"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftWoodenCoinButton.grid(column=2,row=2)

craftCopperCoinButton = tk.Button(text="Craft Copper Coin", command=lambda: [Mint.mintCoins("copper"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftCopperCoinButton.grid(column=2,row=3)

craftIronCoinButton = tk.Button(text="Craft Iron Coin", command=lambda: [Mint.mintCoins("iron"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftIronCoinButton.grid(column=2,row=4)

craftBronzeCoinButton = tk.Button(text="Craft Bronze Coin", command=lambda: [Mint.mintCoins("bronze"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftBronzeCoinButton.grid(column=2,row=5)

craftSilverCoinButton = tk.Button(text="Craft Silver Coin", command=lambda: [Mint.mintCoins("silver"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftSilverCoinButton.grid(column=2,row=6)

craftGoldCoinButton = tk.Button(text="Craft Gold Coin", command=lambda: [Mint.mintCoins("gold"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftGoldCoinButton.grid(column=2,row=7)

craftPlatinumCoinButton = tk.Button(text="Craft Platinum Coin", command=lambda: [Mint.mintCoins("platinum"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlatinumCoinButton.grid(column=2,row=8)

coinButtons = [craftWoodenCoinButton, craftCopperCoinButton, craftIronCoinButton, craftBronzeCoinButton, craftSilverCoinButton, craftGoldCoinButton, craftPlatinumCoinButton]

furnaceLabel = tk.Label(text="Furnace Level " + str(Furnace.level) + "\n" + Furnace.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT * 2)
furnaceLabel.grid(column=3,row=0)
upgradeFurnaceButton = tk.Button(text="Upgrade Furnace", command=lambda: [Furnace.upgrade(Furnace), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeFurnaceButton.grid(column=3,row=1)

craftCopperBarButton = tk.Button(text="Craft Copper Bar", command=lambda: [Furnace.smeltBar("copper"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftCopperBarButton.grid(column=3,row=3)

craftIronBarButton = tk.Button(text="Craft Iron Bar", command=lambda: [Furnace.smeltBar("iron"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftIronBarButton.grid(column=3,row=4)

craftBronzeBarButton = tk.Button(text="Craft Bronze Bar", command=lambda: [Furnace.smeltBar("bronze"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftBronzeBarButton.grid(column=3,row=5)

craftSilverBarButton = tk.Button(text="Craft Silver Bar", command=lambda: [Furnace.smeltBar("silver"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftSilverBarButton.grid(column=3,row=6)

craftGoldBarButton = tk.Button(text="Craft Gold Bar", command=lambda: [Furnace.smeltBar("gold"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftGoldBarButton.grid(column=3,row=7)

craftPlatinumBarButton = tk.Button(text="Craft Platinum Bar", command=lambda: [Furnace.smeltBar("platinum"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlatinumBarButton.grid(column=3,row=8)

barButtons = [craftCopperBarButton, craftIronBarButton, craftBronzeBarButton, craftSilverBarButton, craftGoldBarButton, craftPlatinumBarButton]

checkButtons()

game.mainloop()