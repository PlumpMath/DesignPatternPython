class Product:

    def __init__(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def getTaxPrice(self, TaxVisitor):
        pass

class ProductA(Product):
    def getTaxPrice(self, TaxVisitor):
        return TaxVisitor.taxVisit(self)


class ProductB(Product):
    def getTaxPrice(self, TaxVisitor):
        return TaxVisitor.taxVisit(self)
