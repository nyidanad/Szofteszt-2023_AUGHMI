import unittest
from test1 import LRV

class TestLRV(unittest.TestCase):
  def test_forward_north(self):
    rover = LRV(0, 0, 'N')
    result = rover.move('f')
    self.assertEqual(result, (0, 1, 'N'))


if __name__ == '__main__':
  unittest.main()