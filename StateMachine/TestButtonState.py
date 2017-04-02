import unittest
from ButtonState import ButtonStateOff, ButtonStateOn, ButtonStateInterface

class TestButtonState(unittest.TestCase):
    def test_start(self):
        on=ButtonStateOn()
        self.assertEqual(0, on.__getstate__())

    def test_statusOn(self):
        on=ButtonStateOn()
        ret=on.changeGpioState()
        self.assertEqual(1, on.__getstate__())
        self.assertIsInstance(ret, ButtonStateOff)

    def test_statusOff(self):
        off=ButtonStateOff()
        ret=off.changeGpioState()
        self.assertEqual(0,off.__getstate__())
        self.assertIsInstance(ret, ButtonStateOn)

if __name__ == '__main__':
    unittest.main()
