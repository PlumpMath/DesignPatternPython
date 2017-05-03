class Item:

    def __init__(self, idKey, idValue):
        self.__item = dict()
        self.__item[idKey] = idValue

    def append(self, key, value):
        self.__item[key] = value

    def getItem(self):
        return self.__item

    def __len__(self):
        return self.__item.__sizeof__()
