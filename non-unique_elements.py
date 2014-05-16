""" You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

non-unique-elements

Input: A list of integers.

Output: The list of integers.

How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis for solving more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).

Precondition:
0 < |X| < 1000
"""

import unittest

def checkio(data):
    return filter(lambda e: data.count(e) != 1, data)

class TestCheckio(unittest.TestCase):
    def setUp(self):
        # Perform set up actions (if any)
        pass
    def tearDown(self):
        # Perform clean-up actions (if any)
        pass
    def test1(self):
        self.assertEqual(checkio([1, 2, 3, 1, 3]),
                         [1, 3, 1, 3])
        
    def test2(self):
        self.assertEqual(checkio([1, 2, 3, 4, 5]),
                         [])
        
    def test3(self):
        self.assertEqual(checkio([5, 5, 5, 5, 5]),
                         [5, 5, 5, 5, 5])
        
    def test4(self):
        self.assertEqual(checkio([10, 9, 10, 10, 9, 8]),
                         [10, 9, 10, 10, 9])
        
# Run the unittests                                                                                                    
if __name__ == '__main__':
    unittest.main()
