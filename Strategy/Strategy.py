class Strategy:
    _a = 0
    _b = 0
    _result = 0

    def __init__(self, a, b):

        try:
            int(a)
            int(b)
        except ValueError:
            raise ValueError

        self._a = a
        self._b = b

    def algorithm(self):
        pass

    def getResult(self):
        return self._result

class StrategyAddition(Strategy):
    def algorithm(self):
        self._result = self._a + self._b

class StrategySubtraction(Strategy):
    def algorithm(self):
        self._result = self._a - self._b

