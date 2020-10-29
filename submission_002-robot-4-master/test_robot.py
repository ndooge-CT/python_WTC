import unittest
import robot
from world.text import world as world
from world import obstacles as obstacles
from io import StringIO
from test_base import run_unittests
from test_base import captured_io


class MyTestCase(unittest.TestCase):
    def test_check_observations(self):

        with captured_io(StringIO('HAL\nleft\nforward 10\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
There are some obstacles:
- At position 1,1 (to 5,5)""", output[:107])
    
if __name__ == '__main__':
    unittest.main()