
# Furnace class to consume ore and coal to produce bars

import json
import Treasury
import random
import Building

level = 0
maxLevel = 6
reqs = json.load(open("data/upgradeRequirements.json"))["Furnace"]

global mineCount
mineCount = 0

def mineStone():

    rnd = random.randint(0, 100)

    global mineCount
    mineCount = mineCount + 1
    Treasury.addItem("stone")
    if(rnd > 66):
        Treasury.addItem("coal")
    if(level >= 1 and rnd < 33):
        Treasury.addItem("copper ore")
    if(level >= 2 and rnd < 25):
        Treasury.addItem("iron pre")
    if(level >= 3 and rnd < 15):
        Treasury.addItem("bronze ore")
    if(level >= 4 and rnd < 10):
        Treasury.addItem("silver ore")
    if(level >= 5 and rnd < 7):
        Treasury.addItem("gold ore")
    if(level >= 6 and rnd < 5):
        Treasury.addItem("platinum ore")

def smeltBar(type):
    Treasury.addItem(type + " bar")
    Treasury.removeItem(type + " ore")
    Treasury.removeItem("coal")

def canSmeltBar(type):
    global level
    if level == 0:
        return False
    requiredItem = Treasury.itemSet["ore"].copy()
    requiredItem.addAttribute(type)
    if(Treasury.numberItems(requiredItem.stringifyItem()) > 0 and Treasury.numberItems("coal")):
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