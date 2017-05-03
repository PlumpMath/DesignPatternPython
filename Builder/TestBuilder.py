import unittest
from JsonBuilder import JsonBuilder
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



if __name__ == '__main__':
    unittest.main()
