'''
Created on Mar 20, 2020

@author: marbe
'''
import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):            # runs at start of the test
        print('setupClass')
        
    @classmethod
    def tearDownClass(cls):         # runs at the end of the test
        print('teardownClass')
        
    def setUp(self):                # it runs before any test (test method)
        print('setUp')              # all print statements only for show how it works
        self.emp_1 = Employee('Corey', 'Schafer', 50000) # for every test created new
        self.emp_2 = Employee('Sue', 'Smith', 60000)
    
    def tearDown(self):             # it runs after any test (test method)
        print('tearDown')
        unittest.TestCase.tearDown(self)

    def test_email(self):   
        print('test_email')    
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
        
    def test_fullname(self):
        print('test_fullname')  
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')    
        
    def test_apply_raise(self):
        print('test_apply_raise')  
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
    
    def test_monthly_schedule(self):                # example how to check a get from eg. a website which is down but our code would be still without error
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True       # test fo a good response
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEquals(schedule, 'Success')
            
            mocked_get.return_value.ok = False      # test of a bad response
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEquals(schedule, 'Bad Response!')
                                   
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()