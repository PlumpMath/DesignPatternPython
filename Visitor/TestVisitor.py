import unittest
from Visitor import TaxAustria, TaxGermany
from Product import ProductA, ProductB

class VisitorTestCase(unittest.TestCase):
    def test_TaxAustriaProductA(self):
        taxAut = TaxAustria()
        prodA = ProductA(1.0)
        priceWithTax = prodA.getTaxPrice(taxAut)
        self.assertEqual(1.20, priceWithTax)

    def test_TaxAustriaProductB(self):
        taxAut = TaxAustria()
        prodB = ProductB(1.0)
        priceWithTax = prodB.getTaxPrice(taxAut)
        self.assertEqual(1.10, priceWithTax)

    def test_TaxGermanyProductA(self):
        taxGer=TaxGermany()
        prodA=ProductA(1.0)
        priceWithTax=prodA.getTaxPrice(taxGer)
        self.assertEqual(1.50, priceWithTax)

    def test_TaxGermanyProductB(self):
        taxGer=TaxGermany()
        prodB=ProductB(1.0)
        priceWithTax=prodB.getTaxPrice(taxGer)
        self.assertEqual(1.60, priceWithTax)

if __name__ == '__main__':
    unittest.main()
