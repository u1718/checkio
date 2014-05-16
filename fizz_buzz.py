""" "Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.

Tips: You can easily solve this task with: if-else, % operator and string conversion.

Input: A number as an integer.

Output: The string.

Precondition: 0 < number <= 1000
"""

import unittest

def checkio(number):
    fbm = {0: lambda p: str(p),
           1: lambda p: "Fizz",       # %3
           2: lambda p: "Buzz",       # %5
           3: lambda p: "Fizz Buzz"}  # %15

    return fbm[((number % 5 == 0) << 1) | (number % 3 == 0)](number) 
        
class TestCheckio(unittest.TestCase):
    def setUp(self):
        # Perform set up actions (if any)
        pass
        
    def tearDown(self):
        # Perform clean-up actions (if any)
        pass
        
    def test1(self):
        self.assertEqual(checkio(15), "Fizz Buzz") # "15 is divisible by 3 and 5"
        
    def test2(self):
        self.assertEqual(checkio(6), "Fizz") # "6 is divisible by 3"
        
    def test3(self):
        self.assertEqual(checkio(5), "Buzz") # "5 is divisible by 5"
        
    def test4(self):
        self.assertEqual(checkio(7), "7") # "7 is not divisible by 3 or 5"
                         
# Run the unittests
if __name__ == '__main__':
    unittest.main()
