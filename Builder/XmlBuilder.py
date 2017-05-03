from Builder import Builder

class XmlBuilder(Builder):

    def __init__(self):
        pass

    def getResult(self):
        items = Builder().getItems()
        xml = "<list>"
        xmlContent = ""

        for item in items:
            xmlContent = xmlContent + self.getPartElement(item.getItem())

        xml = xml + xmlContent+"</list>"
        return xml


    def getPartElement(self, elements):
        itemStr = "<item>"

        for key in elements:
            itemStr = itemStr + "<{}>{}</{}>".format(str(key),str(elements[key]), str(key))

        return itemStr+"</item>"