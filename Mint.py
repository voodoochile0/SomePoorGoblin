
# Mint class to consume bars to produce coins

import json
import Treasury

global level
level = 0
reqs = json.load(open("data/upgradeRequirements.json"))["Mint"]
plank = Treasury.itemSet["plank"].copy()
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

def mintCoins(type):
    match type:
        case "wooden":
            Treasury.removeItem(plank)
        case "copper":
            Treasury.removeItem(copperBar)
        case "iron":
            Treasury.removeItem(ironBar)
        case "bronze":
            Treasury.removeItem(bronzeBar)
        case "silver":
            Treasury.removeItem(silverBar)
        case "gold":
            Treasury.removeItem(goldBar)
        case "platinum":
            Treasury.removeItem(platinumBar)

    coin = Treasury.itemSet["coin"].copy()
    coin.addAttribute(type)

    for i in range(5):
        Treasury.addItem(coin)

def canCraft(type):
    global level
    if level == 0:
        return False
    if type == "wooden":
        if(Treasury.numberItems("plank") > 0):
            return True
    requiredItem = Treasury.itemSet["bar"].copy()
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
        strReqs = strReqs + key + " " + str(reqs[key]) + "\n"

    return strReqs[0: len(strReqs) - 1]