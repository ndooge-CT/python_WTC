import sys
import robot
import unittest
from world.text import world as world
from test_base import captured_io
from test_base import run_unittests
from io import StringIO
from world import obstacles as obstacles
sys.path.append('/homes/ndooge/problems/submission_002-robot-4/world/')


class MyTestCase(unittest.TestCase):
    def test_start_world(self):
        world.start_world()
        world.update_position(51)
        world.show_position("hal")


if __name__ == '__main__':
    unittest.main()
