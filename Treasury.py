import pprint
import Item

# Inventory class that contains item objects and their quantaties in a dictionary

global items
global itemSet

items = {}
itemSet = {}

input = open("data/items.txt", "r").read().split("\n")
attr = open("data/attributes.txt", "r").read().split("\n")

for i in range(input.__len__()):
    currentItem = input[i].split(" ")
    itemName = currentItem[0]
    thing = Item.Item(itemName, float(currentItem[1]))
    itemSet[thing.stringifyItem()] = thing

def addItem(stringify):
    for key in items.keys():
        if key.stringifyItem() == stringify:
            count = items[key] + 1
            items[key] = count
            return
    stringify = stringify.split(" ")
    item = itemSet[stringify[len(stringify) - 1]].copy()
    if(len(stringify) > 1):
        item.addAttribute(stringify[0])
    items[item] = 1

def numberItems(stringify):
    for key in items.keys():
        if key.stringifyItem() == stringify:
            return items[key]
    return 0

def removeItem(item):
    for key in items.keys():
        if key.stringifyItem() == stringify:
            count = items[key] - 1
            items[key] = count
            return

def totalValue():
    total = 0.0
    for value in items.values():
        total = total + value
    return total

def stringify():
    string = ""
    for key in items.keys():
        string = string + key.stringifyItem() + " " + str(items[key]) + " " + str(key.value) + "\n"
    return string

def generateStartingStash():
    addItem("stone axe")
    addItem("stone pickaxe")
    addItem("log")