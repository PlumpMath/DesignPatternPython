from Product import ProductA, ProductB
from multimethod import multimethod


class TaxVisitor:
    def taxVisit(self, ProductA):
        pass

    def taxVisit(self, ProductB):
        pass

class TaxAustria(TaxVisitor):
    @multimethod(object, ProductA)
    def taxVisit(self, ProductA):
        print('Product A - Tax calculation AUT')
        return ProductA.getPrice() * 1.20

    @multimethod(object, ProductB)
    def taxVisit(self, ProductB):
        print('Product B - Tax calculation AUT')
        return ProductB.getPrice() * 1.10

class TaxGermany(TaxVisitor):
    @multimethod(object, ProductA)
    def taxVisit(self, ProductA):
        print('Product A - Tax calculation GER')
        return ProductA.getPrice() * 1.50

    @multimethod(object, ProductB)
    def taxVisit(self, ProductB):
        print ('Product B - Tax calculation GER')
        return ProductB.getPrice() * 1.60