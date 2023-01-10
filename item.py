
# Item class that has the item, it's value, and any activeAttributes that it may or may not have

class Item:

    name = ""
    value = 0.0
    allAttributes = {}

    ## STATIC VARS
    activeAttributes = {}
    ATTRFILE = "data/attributes.txt"

    input = open(ATTRFILE, "r").read().split("\n")

    for i in range(input.__len__()):
        currentAttr = input[i].split(" ")
        attrName = currentAttr[0]
        attrContr = float(currentAttr[1])
        allAttributes[attrName] = attrContr

    def __init__(self, name, value):
        self.name = name
        self.value = float(value)
        self.activeAttributes = {}

    def addAttribute(self, attribute):
        if(not self.activeAttributes.keys().__contains__(attribute)):
            self.activeAttributes[attribute] = self.allAttributes[attribute]
            self.value = self.value * self.allAttributes[attribute]

    def removeAttribute(self, attribute):
        if(self.activeAttributes().keys().__contains__(attribute)):
            self.value = self.value / self.allAttributes[attribute]
            self.activeAttributes.pop(attribute)

    def stringify(self):
        string = ""
        for key in self.activeAttributes.keys():
            string = string + key + " "
        string = string + self.name
        return string
    