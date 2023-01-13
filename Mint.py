
# Mint class to consume bars to produce coins

import json
import Treasury
import Building

maxLevel = 7

global level
level = 0
reqs = json.load(open("data/upgradeRequirements.json"))["Mint"]

def mintCoins(type):
    if type == "wooden":
        Treasury.removeItem("plank")
    else:
        Treasury.removeItem(type + " bar")

    for i in range(5):
        Treasury.addItem(type + " coin")

def canCraft(type):
    global level
    if level == 0:
        return False
    if type == "wooden":
        if(Treasury.numberItems("plank") > 0):
            return True
    requiredItem = type + " bar"
    if(Treasury.numberItems(requiredItem) > 0):
        return True
    return False

def upgrade(self):
    Building.upgrade(self)

def canUpgrade(self):
    Building.canUpgrade(reqs[str(level) + 1])

def buildReqs():
    Building.buildReqs()

def buildReqsStr():
    Building.buildReqsStr()

def upgrade(self):
    toRemove = buildReqs()
    for key in toRemove.keys():
        for i in range(toRemove[key]):
            Treasury.removeItem(key)
    self.level = self.level + 1

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