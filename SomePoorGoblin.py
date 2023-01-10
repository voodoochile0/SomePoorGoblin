
import Item

treasury = {}

itemSet = []
attributeSet = []

def generateItems(filename):

def generateAttributes(filename):
    input = open(filename, "r").read().split("\n")

    for i in range(input.__len__()):
        currentItem = input[i].split(" ")
        thing = Item(currentItem[0], currentItem[1])
    