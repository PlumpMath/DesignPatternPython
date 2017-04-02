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

    def test_invalideValue(self):
        with self.assertRaises(ValueError) as cm:
            StrategyAddition('A', 3)

        self.assertTrue(isinstance(cm.exception, ValueError))


if __name__ == '__main__':
    unittest.main()
