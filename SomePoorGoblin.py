
import Item
import Inventory

treasury = Inventory.Inventory()

itemSet = {}
attributeSet = {}
ITEMFILE = "data/items.txt"
ATTRFILE = "data/attributes.txt"

def generateItems(filename):
    
    input = open(filename, "r").read().split("\n")

    for i in range(input.__len__()):
        currentItem = input[i].split(" ")
        print(currentItem)
        itemName = currentItem[0]
        thing = Item.Item(itemName, float(currentItem[1]))
        itemSet[itemName] = thing


# def generateAttributes(filename):

#     input = open(filename, "r").read().split("\n")

#     for i in range(input.__len__()):
#         currentAttr = input[i].split(" ")
#         attrName = currentAttr[0]
#         attrContr = currentAttr[1]
#         attributeSet[attrName] = attrContr
    
generateItems(ITEMFILE)

axe = itemSet["axe"]
axe.addAttribute("copper")
pickaxe = itemSet["pickaxe"]
pickaxe.addAttribute("platinum")
pickaxe.addAttribute("platinum-plated")
treasury.addItem(axe)
treasury.addItem(pickaxe)
print(treasury.stringify())