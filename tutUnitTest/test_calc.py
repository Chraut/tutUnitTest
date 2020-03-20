'''
Created on Mar 19, 2020

@author: marbe
'''
import unittest
import calc

class TestCalc(unittest.TestCase):


    def test_add(self):                     # first word must be 'test'
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):                # first word must be 'test'
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    
    def test_multiply(self):                # first word must be 'test'
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        
    def test_devide(self):                  # first word must be 'test'
        self.assertEqual(calc.devide(10, 5), 2)
        self.assertEqual(calc.devide(-1, 1), -1)
        self.assertEqual(calc.devide(-1, -1), 1)
        self.assertEqual(calc.devide(5, 2), 2.5)
        
        #self.assertRaises(ValueError, calc.devide, 10, 0)   # 1 possibility to check if ValueError comes ba
        
        with self.assertRaises(ValueError):  # better with this for exepction
            calc.devide(10, 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
