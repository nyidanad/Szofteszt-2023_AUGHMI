import unittest
from test1 import LRV

class TestLRV(unittest.TestCase):
  def test_forward_north(self):
    rover = LRV(0, 0, 'N', [])
    result = rover.move('f')
    self.assertEqual(result, (0, 1, 'N'))

  def test_forward_south(self):
    rover = LRV(0, 0, 'S', [])
    result = rover.move('f')
    self.assertEqual(result, (0, -1, 'S'))

  def test_forward_east(self):
    rover = LRV(0, 0, 'E', [])
    result = rover.move('f')
    self.assertEqual(result, (1, 0, 'E'))

  def test_forward_west(self):
    rover = LRV(0, 0, 'W', [])
    result = rover.move('f')
    self.assertEqual(result, (-1, 0, 'W'))

  def test_backward(self):
    rover = LRV(0, 0, 'E', [])
    result = rover.move('b')
    self.assertEqual(result, (1, 0, 'E'))

  def test_left(self):
    rover = LRV(0, 0, 'N', [])
    result = rover.move('l')
    self.assertEqual(result, (0, 0, 'W'))

  def test_right(self):
    rover = LRV(0, 0, 'E', [])
    result = rover.move('r')
    self.assertEqual(result, (0, 0, 'S'))

  def test_obstacle(self):
    rover = LRV(0, 0, 'N', [(0, 1)])
    result = rover.move('f')
    self.assertEqual(result, "WARNING: Obstacle!")

if __name__ == '__main__':
  unittest.main()