import random
import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot

class MyTestCase(unittest.TestCase):
    def test_step6_replay_range_basic_reversed(self):
        with captured_io(StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 2 reversed\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,8).
 > HAL moved forward by 3 steps.
 > HAL now at position (0,11).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..""", output)


if __name__ == '__main__':
    unittest.main()
