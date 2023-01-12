
# Sawmill class to consumes logs to create planks

import json
import Treasury

global level
level = 0
reqs = json.load(open("data/upgradeRequirements.json"))["Sawmill"]

log = Treasury.itemSet["log"].copy()
plank = Treasury.itemSet["plank"].copy()

def gatherWood():
    Treasury.addItem(log)

def craftPlank():
    Treasury.removeItem(log)
    for i in range(level):
        Treasury.addItem(plank)

def canCraftPlank():
    if Treasury.numberItems("log") > 0 and level > 0:
        return True
    return False

def upgrade():
    toRemove = buildReqs()
    for key in toRemove.keys():
        item = Treasury.itemSet[key]
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