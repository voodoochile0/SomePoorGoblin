
# Inventory class that contains item objects and their quantaties in a dictionary

class Inventory:

    items = {}

    def __init__(self):
        pass

    def addItem(self, item):
        if(self.items.keys().__contains__(item)):
            count = self.items[item] + 1
            self.items[item] = count
        else:
            self.items[item] = 1


    def removeItem(self, item):
        if(self.items.keys().__contains__(item)):
            count = self.items[item] - 1
            self.items[item] = count
            if(count == 0):
                self.items.pop(item)

    def items(self):
        return self.items

    def totalValue(self):
