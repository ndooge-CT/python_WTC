from maze import obstacles as obstacles
import unittest
import robot


class MyTestCase(unittest.TestCase):

    def test_is_path_blocked(self):
        obstacles.set_obstacles([(5, 0), (10, 15)])
        self.assertEqual(obstacles.is_path_blocked(5, 5, 5, -2), True)


if __name__ == '__main__':
    unittest.main()
