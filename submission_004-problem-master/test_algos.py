import unittest
import sys
from test_base import run_unittests
import super_algos


class MyTestCase(unittest.TestCase):
    def test_step1_find_min_empty1(self):
        result = super_algos.find_min([])
        self.assertEqual(-1, result)
    def test_step1_find_min_valid(self):
        result = super_algos.find_min([5,19,12,33,2,1])
        self.assertEqual(1, result)

    def test_step1_find_min_one_element(self):
        result = super_algos.find_min([5])
        self.assertEqual(5, result)

    def test_step1_find_min_negative(self):
        result = super_algos.find_min([2,200,-201,2,-2])
        self.assertEqual(-201, result)

    def test_step1_find_min_invalid(self):
        result = super_algos.find_min(['x',100,'s',4,-5])
        self.assertEqual(-1, result)

    def test_step2_sum_all_empty_list(self):
        result = super_algos.sum_all([])
        self.assertEqual(-1, result)

    def test_step2_sum_all_valid(self):
        result = super_algos.sum_all([1,2,3])
        self.assertEqual(6, result)

    def test_step2_sum_all_one_element(self):
        result = super_algos.sum_all([6])
        self.assertEqual(6, result)

    def test_step2_sum_all_negative(self):
        result = super_algos.sum_all([-2,-3,-5])
        self.assertEqual(-10, result)

    def test_step2_sum_all_invalid_elements(self):
        result = super_algos.sum_all(['x',900,'c',5,-66])
        self.assertEqual(-1, result)

    def test_step3_find_strings_one(self):
        result = super_algos.find_possible_strings(['a','b','c'], 1)
        self.assertEqual(['a','b','c'], result)

    def test_step3_find_strings_three(self):
        result = super_algos.find_possible_strings(['x','y'], 3)
        self.assertEqual(['xxx', 'xxy', 'xyx', 'xyy', 'yxx', 'yxy', 'yyx', 'yyy'], result)

    def test_step3_find_strings_empty(self):
        result = super_algos.find_possible_strings([], 3)
        self.assertEqual([], result)

    def test_step3_find_strings_not_chars(self):
        result = super_algos.find_possible_strings([1,2,3,4], 3)
        self.assertEqual([], result)

    
if __name__ == '__main__':
    unittest.main()