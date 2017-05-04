from Builder import Builder

class JsonBuilder(Builder):

    def __init__(self):
        pass

    def getResult(self):
        items = Builder().getItems()
        json = "{"
        itemsSize = len(items)
        currentItem = 0
        jsonContent = ""
        for item in items:
            currentItem = currentItem +1
            jsonContent = jsonContent + self.getPartElement(item.getItem())
            if(currentItem < itemsSize):
                jsonContent = jsonContent+","

        json = json +jsonContent+"}"
        return json

    def getPartElement(self, elements):
        itemStr = ""
        itemSize = len(elements)
        currentItem = 0
        for key in elements:
            currentItem = currentItem + 1
            itemStr = itemStr + "\"{}\":\"{}\"".format(str(key),str(elements[key]))
            if(currentItem < itemSize):
                itemStr = itemStr+", "

        return "{" + itemStr + "}"
