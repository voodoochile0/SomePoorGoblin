import SomePoorGoblin

# Item class that has the item, it's value, and any attributes that it may or may not have

class Item:

    name = ""
    value = 0.0
    attributes = {}

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def addAttribute(self, attribute):
        if(self.attributes.keys().__contains__(attribute)):
            self.attributes[attribute] = SomePoorGoblin.attributeSet[attribute]
            self.value = self.value * self.attributes[attribute]

    def removeAttribute(self, attribute):
        if(self.attributes.keys().__contains__(attribute)):
            self.value = self.value / self.attributes[attribute]
            self.attributes.pop(attribute)


    def value(self):
        return self.value

    def attributes(self):
        return self.attributes
    