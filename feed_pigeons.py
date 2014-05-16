"""I start to feed one of the pigeons. A minute later two more fly by and a minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute, but in case there's not enough food for all the birds, the pigeons who arrived first ate first. Pigeons are hungry animals and eat without knowing when to stop. If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?

pigeons

Input: A quantity of portions wheat, a positive integer.

Output: The number of fed pigeons, an integer.

Precondition: 0 < N < 105.
"""

import unittest

def checkio(number):
    pigeons = 0
    n = 0
    while True:
        n += 1
        pigeons += n
        number -= pigeons
        if number <= 0:
            pigeons = max(pigeons - n, number + pigeons)
            break
            
    return pigeons
    
class TestCheckio(unittest.TestCase):
    def setUp(self):
        # Perform set up actions (if any)
        pass
        
    def tearDown(self):
        # Perform clean-up actions (if any)
        pass
        
    def test1(self):
        self.assertEqual(checkio(1), 1)
        
    def test2(self):
        self.assertEqual(checkio(2), 1)
        
    def test3(self):
        self.assertEqual(checkio(3), 2)
        
    def test4(self):
        self.assertEqual(checkio(4), 3)
        
    def test5(self):
        self.assertEqual(checkio(5), 3)
        
    def test6(self):
        self.assertEqual(checkio(10), 6)

# Run the unittests
if __name__ == '__main__':
    unittest.main()

