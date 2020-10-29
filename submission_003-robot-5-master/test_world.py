import sys
import robot
import unittest
from world.text import world as world
from test_base import captured_io
from test_base import run_unittests
from io import StringIO
from maze import obstacles as obstacles
sys.path.append('/homes/ndooge/problems/submission_002-robot-4/world/')


class MyTestCase(unittest.TestCase):
    def test_start_world(self):
        return False


if __name__ == '__main__':
    unittest.main()
