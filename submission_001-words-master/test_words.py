import word_processor
import unittest
from test_base import run_unittests

class MyWordProcessorTest(unittest.TestCase):
    def test_step1(self):
        self.assertEqual(word_processor.convert_to_word_list(
            'Time for a new age, one where we are unified!'),['time','for','a','new','age','one','where','we','are','unified']) 

    def test_step2(self):
        self.assertEqual(word_processor.words_longer_than(4,"Hello my name is TRON"),["hello"])

    def test_step3(self):
        self.assertEqual(word_processor.words_lengths_map("Hello my name is TRON"),{5: 1, 2: 2, 4: 2})
if __name__ == '__main__':
    unittest.main()