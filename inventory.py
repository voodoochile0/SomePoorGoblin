import pprint

# Inventory class that contains item objects and their quantaties in a dictionary

class Inventory:

    items = {}

    def Inventory(self):
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

    def stringify(self):
        string = ""
        for key in self.items.keys():
            string = string + key.stringify() + " " + str(self.items[key]) + " " + str(key.value) + "\n"
        return string