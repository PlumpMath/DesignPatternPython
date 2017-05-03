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

    def getPartElement(self, itemElements):
        itemStr = ""
        itemSize = len(itemElements)
        currentItem = 0
        for key in itemElements:
            currentItem = currentItem + 1
            itemStr = itemStr + "\"{}\":\"{}\"".format(str(key),str(itemElements[key]))
            if(currentItem < itemSize):
                itemStr = itemStr+", "

        return "{" + itemStr + "}"
