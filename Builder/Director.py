class Director:

    __concreteBuilder = None

    def __init__(self, concretBuilder):
        Director.__concreteBuilder = concretBuilder

    def construct(self):
       return  Director.__concreteBuilder.getResult()

