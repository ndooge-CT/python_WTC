from mastermind import *
import unittest
from unittest.mock import patch
from io import StringIO

def test_create_code():
    for i in range(100):
        code = create_code()
        print(code)
def test_check_correctness(a,b):
    correct = check_correctness(a,b)
    print (correct)
test_create_code()
test_check_correctness(2,2)
test_check_correctness(5,4)
class TestFunctions(unittest.TestCase):
    @patch("sys.stdin", StringIO("1234\n4567\n"))
    def test_compare(self):
        self.assertEqual(get_answer_input(), "1234")
        self.assertEqual(get_answer_input(), "4567")

    