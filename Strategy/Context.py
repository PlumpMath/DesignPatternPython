class Context:

    _strategy = None

    def __init__(self, strategy):
        Context._strategy = strategy

    def execute(self):
        Context._strategy.algorithm()
        return Context._strategy.getResult()