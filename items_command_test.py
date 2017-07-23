
from cfunctions import items_command
import rooms
import unittest

class ItemCommand(unittest.TestCase):
   def test_beach(self):
       self.assertTrue(items_command(rooms.beach1) == 'coconut, coconut, coconut, rope, seagull')

if __name__ == '__main__':
   unittest.main()
