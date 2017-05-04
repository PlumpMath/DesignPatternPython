class Builder:

    __items = list()

    def __init__(self):
        pass

    def getResult(self):
        pass

    def getPartElement(self, element):
        pass

    def append(self, item):
        self.__items.append(item)

    def getItems(self):
        return self.__items

