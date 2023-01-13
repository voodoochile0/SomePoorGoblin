import Treasury

def upgrade(self):
    toRemove = self.buildReqs()
    for key in toRemove.keys():
        for i in range(toRemove[key]):
            Treasury.removeItem(key)
    self.level = self.level + 1

def canUpgrade(self, reqs):
    if(self.level < self.maxLevel):
        currentReqs = reqs[str(self.level + 1)]
        for thing in currentReqs.keys():
            if not Treasury.numberItems(thing) >= currentReqs[thing]:
                return False

        return True

def buildReqs(self, reqs):
    return reqs[str(self.level + 1)]

def buildReqsStr():
    reqs = buildReqs()
    strReqs = ""
    for key in reqs.keys():
        strReqs = strReqs + key + " " + str(reqs[key]) + "\n"
    return strReqs[0: len(strReqs) - 1]