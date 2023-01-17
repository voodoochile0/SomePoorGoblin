import pprint
import Item

# Inventory class that contains item objects and their quantaties in a dictionary

global items
global itemSet

items = {}
itemSet = {}

input = open("data/items.txt", "r").read().split("\n")
attr = open("data/attributes.txt", "r").read().split("\n")

def generateStartingStash():
    pass

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

def removeItem(stringify):
    for key in items.keys():
        if key.stringifyItem() == stringify:
            count = items[key] - 1
            items[key] = count
            return

def totalValue():
    total = 0.0
    for item in items.keys():
        total += (item.value * items[item])
    return total

def coinsValue():
    total = 0.0
    for key in items.keys():
        if key.name == "coin":
            total += items[key] * key.value

def stringifyRawMaterials():
    ores = ""
    raw = ""
    values = ""
    names = ""
    quant = ""
    for key in items.keys():
        if key.name == "log":
            raw = raw + key.stringifyItem() + " " + str(items[key]) + " "
            names += (key.stringifyItem()+"\n")
            quant += (str(items[key])+"\n")
            values += (str(items[key] * key.value)+"\n")
        elif key.name == "stone":
            raw = raw + key.stringifyItem() + " " + str(items[key]) + " "
            names += (key.stringifyItem()+"\n")
            quant += (str(items[key])+"\n")
            values += (str(items[key] * key.value)+"\n")
        elif key.name == "coal":
            raw = raw + key.stringifyItem() + " " + str(items[key]) + " "
            names += (key.stringifyItem()+"\n")
            quant += (str(items[key])+"\n")
            values += (str(items[key] * key.value)+"\n")
        elif key.name == "ore":
            ores = ores + key.stringifyItem() + " " + str(items[key]) + " "
            names += (key.stringifyItem()+"\n")
            quant += (str(items[key])+"\n")
            values += (str(items[key] * key.value)+"\n")

    return [names, quant, values]

def stringifyBars():
    bars = ""
    names = ""
    quant = ""
    values = ""
    for key in items.keys():
        if key.name == "bar":
            bars = bars + key.stringifyItem() + " " + str(items[key]) + " "
            names += (key.stringifyItem()+"\n")
            quant += (str(items[key])+"\n")
            values += (str(items[key] * key.value)+"\n")
    return [names, quant, values]

def stringifyCoins():
    bars = ""
    names = ""
    quant = ""
    values = ""
    for key in items.keys():
        if key.name == "coin":
            bars = bars + key.stringifyItem() + " " + str(items[key]) + " "
            names += (key.stringifyItem()+"\n")
            quant += (str(items[key])+"\n")
            values += (str(items[key] * key.value)+"\n")
    return [names, quant, values]

def stringifyArms():
    spears = ""
    armor = ""
    names = ""
    quant = ""
    values = ""
    for key in items.keys():
        if key.name == "spear":
            spears = spears + key.stringifyItem() + " " + str(items[key]) + " "
            names += (key.stringifyItem()+"\n")
            quant += (str(items[key])+"\n")
            values += (str(items[key] * key.value)+"\n")
        if key.name == "armor":
            armor = armor + key.stringifyItem() + " " + str(items[key]) + " "
            names += (key.stringifyItem()+"\n")
            quant += (str(items[key])+"\n")
            values += (str(items[key] * key.value)+"\n")
    return [names, quant, values]

def stringify():
    raw = ""
    ores = ""
    bars = ""
    coins = ""
    armor = ""
    spears = ""

    for key in items.keys():
        if key.name == "coin":
            coins = coins + key.stringifyItem() + " " + str(items[key]) + " " + str(key.value * items[key]) + "\n"
        elif key.name == "ore":
            ores = ores + key.stringifyItem() + " " + str(items[key]) + " " + str(key.value * items[key]) + "\n"        
        elif key.name == "bar":
            bars = bars + key.stringifyItem() + " " + str(items[key]) + " " + str(key.value * items[key]) + "\n"
        elif key.name == "armor":
            armor = armor + key.stringifyItem() + " " + str(items[key]) + " " + str(key.value * items[key]) + "\n"
        elif key.name == "spear":
            spears = spears + key.stringifyItem() + " " + str(items[key]) + " " + str(key.value * items[key]) + "\n"
        else:
            raw = raw + key.stringifyItem() + " " + str(items[key]) + " " + str(key.value * items[key]) + "\n"
    return raw + "\n" + ores + "\n" + bars + "\n" + coins + "\n"  + spears + "\n"  + armor
