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
    if(Mint.canCraft("wooden")):
        craftWoodenCoinButton.grid()
    else:
        craftWoodenCoinButton.grid_remove()

    if(Furnace.canUpgrade()):
        upgradeFurnaceButton.grid()
    else:
        upgradeFurnaceButton.grid_remove()
    if(Furnace.canSmeltBar("copper")):
        smeltCopperBarButton.grid()
    else:
        smeltCopperBarButton.grid_remove()

game = tk.Tk()

treasuryLabel = tk.Label(text=Treasury.stringify())
treasuryLabel.grid(column=0,row=2)

chopWoodButton = tk.Button(text="Chop Wood", command=lambda: [Sawmill.gatherWood(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
chopWoodButton.grid(column=0,row=0)

mineStone = tk.Button(text="Mine Stone", command=lambda: [Furnace.mineStone(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
mineStone.grid(column=0,row=1)


sawmillLabel = tk.Label(text="Sawmill Level " + str(Sawmill.level) + "\n" + Sawmill.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT)
sawmillLabel.grid(column=1,row=0)
upgradeSawmillButton = tk.Button(text="Upgrade Sawmill", command=lambda: [Sawmill.upgrade(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeSawmillButton.grid(column=1,row=1)

craftPlankButton = tk.Button(text="Craft Plank", command=lambda: [Sawmill.craftPlank(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftPlankButton.grid(column=1,row=2)


mintLabel = tk.Label(text="Mint Level " + str(Mint.level) + "\n" + Mint.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT)
mintLabel.grid(column=2,row=0)
upgradeMintButton = tk.Button(text="Upgrade Mint", command=lambda: [Mint.upgrade(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeMintButton.grid(column=2,row=1)

craftWoodenCoinButton = tk.Button(text="Craft Wooden Coin", command=lambda: [Mint.mintCoins("wooden"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
craftWoodenCoinButton.grid(column=2,row=2)


furnaceLabel = tk.Label(text="Furnace Level " + str(Furnace.level) + "\n" + Furnace.buildReqsStr(), width=GRIDWIDTH, height=GRIDHEIGHT)
furnaceLabel.grid(column=3,row=0)
upgradeFurnaceButton = tk.Button(text="Upgrade Furnace", command=lambda: [Furnace.upgrade(), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
upgradeFurnaceButton.grid(column=2,row=1)

smeltCopperBarButton = tk.Button(text="Smelt Copper Bar", command=lambda: [Furnace.smeltBar("copper"), update_game()], width=GRIDWIDTH, height=GRIDHEIGHT)
smeltCopperBarButton.grid(column=2,row=2)

checkButtons()

game.mainloop()