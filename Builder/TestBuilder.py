import unittest
from JsonBuilder import JsonBuilder
from XmlBuilder import XmlBuilder
from Director import Director
from Item import Item


class MyTestCase(unittest.TestCase):

    def test_jsonBuilder(self):
        item1 = Item("id",1)
        item1.append("lastName", "Muster")
        item1.append("firstName", "Max")

        item2 = Item("id",2)
        item2.append("lastName", "Müller")
        item2.append("firstName", "Ute")

        builder = JsonBuilder()
        builder.append(item1)
        builder.append(item2)

        director = Director(builder)
        json = director.construct()
        self.assertEqual('{{"id":"1", "lastName":"Muster", "firstName":"Max"},{"id":"2", "lastName":"Müller", "firstName":"Ute"}}', json)

    def test_xmlBuilder(self):
        item1 = Item("id",1)
        item1.append("lastName", "Muster")
        item1.append("firstName", "Max")

        item2 = Item("id",2)
        item2.append("lastName", "Müller")
        item2.append("firstName", "Ute")

        builder = XmlBuilder()
        builder.append(item1)
        builder.append(item2)

        director = Director(builder)
        xml = director.construct()
        self.assertEqual("<list><item><id>1</id><lastName>Muster</lastName><firstName>Max</firstName></item><item><id>2</id><lastName>Müller</lastName><firstName>Ute</firstName></item></list>", xml)

if __name__ == '__main__':
    unittest.main()
