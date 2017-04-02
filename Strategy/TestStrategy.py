import unittest
from Context import Context
from Strategy import StrategySubtraction, StrategyAddition, Strategy


class TestCaseStrategy(unittest.TestCase):
    def test_subtraction(self):
        substraction = StrategySubtraction(3, 2)
        context = Context(substraction)
        result = context.execute()

        self.assertEqual(1, result)

    def test_addition(self):
        addition = StrategyAddition(2,1)
        context = Context(addition)
        result = context.execute()
        self.assertEqual(3, result)


if __name__ == '__main__':
    unittest.main()
