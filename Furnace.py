
# Furnace class to consume ore and coal to produce bars

import json
import Treasury

level = 0
reqs = json.load(open("data/upgradeRequirements.json"))["Furnace"]

global mineCount
mineCount = 0

stone = Treasury.itemSet["stone"].copy()
copperBar = Treasury.itemSet["bar"].copy()
copperBar.addAttribute("copper")
ironBar = Treasury.itemSet["bar"].copy()
ironBar.addAttribute("bronze")
bronzeBar = Treasury.itemSet["bar"].copy()
bronzeBar.addAttribute("bronze")
silverBar = Treasury.itemSet["bar"].copy()
silverBar.addAttribute("silver")
goldBar = Treasury.itemSet["bar"].copy()
goldBar.addAttribute("gold")
platinumBar = Treasury.itemSet["bar"].copy()
platinumBar.addAttribute("platinum")

copperOre = Treasury.itemSet["ore"].copy()
copperOre.addAttribute("copper")
ironOre = Treasury.itemSet["ore"].copy()
ironOre.addAttribute("bronze")
bronzeOre = Treasury.itemSet["ore"].copy()
bronzeOre.addAttribute("bronze")
silverOre = Treasury.itemSet["ore"].copy()
silverOre.addAttribute("silver")
goldOre = Treasury.itemSet["ore"].copy()
goldOre.addAttribute("gold")
platinumOre = Treasury.itemSet["ore"].copy()
platinumOre.addAttribute("platinum")

def mineStone():
    global mineCount
    mineCount = mineCount + 1
    Treasury.addItem(stone)
    if(level >= 1 and mineCount % 5):
        Treasury.addItem(copperOre)
    if(level >= 2 and mineCount % 10):
        Treasury.addItem(ironOre)
    if(level >= 3 and mineCount % 15):
        Treasury.addItem(bronzeOre)
    if(level >= 4 and mineCount % 20):
        Treasury.addItem(silverOre)
    if(level >= 5 and mineCount % 25):
        Treasury.addItem(goldOre)
    if(level >= 6 and mineCount % 30):
        Treasury.addItem(platinumOre)

def smeltBar(type):
    match type:
        case "copper":
            Treasury.addItem(copperBar)
            Treasury.removeItem(copperOre)
        case "iron":
            Treasury.addItem(ironBar)
            Treasury.removeItem(ironOre)
        case "bronze":
            Treasury.addItem(bronzeBar)
            Treasury.removeItem(bronzeOre)
        case "silver":
            Treasury.addItem(silverBar)
            Treasury.removeItem(silverOre)
        case "gold":
            Treasury.addItem(goldBar)
            Treasury.removeItem(goldOre)
        case "platinum":
            Treasury.addItem(platinumBar)
            Treasury.removeItem(platinumOre)

def canSmeltBar(type):
    global level
    if level == 0:
        return False
    requiredItem = Treasury.itemSet["ore"].copy()
    requiredItem.addAttribute(type)
    if(Treasury.numberItems(requiredItem.stringifyItem()) > 0):
        return True
    return False

def upgrade():
    toRemove = buildReqs()
    for key in toRemove.keys():
        item = Treasury.itemSet[key].copy()
        for i in range(toRemove[key]):
            Treasury.removeItem(item)
    global level
    level = level + 1

def canUpgrade():
    if(level < 5):
        currentReqs = reqs[str(level + 1)]

        for thing in currentReqs.keys():
            if not Treasury.numberItems(thing) >= currentReqs[thing]:
                return False

        return True

def buildReqs():
    return reqs[str(level + 1)]

def buildReqsStr():
    reqs = buildReqs()
    strReqs = ""
    for key in reqs.keys():
        strReqs = strReqs + key + " " +  str(reqs[key]) + "\n"
    return strReqs[0: len(strReqs) - 1]