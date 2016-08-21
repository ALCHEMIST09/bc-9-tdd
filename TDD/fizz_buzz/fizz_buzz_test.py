import unittest

from fizz_buzz import fizz_buzz

class FizzBuzzTest(unittest.TestCase):
    '''
        Takes in a number and returns "fizz", "buzz", "fizz_buzz" 
        if the number is divisible by 3, 5 or both 3 and 5. If the
        is not divisible by any of the above divisors, return the 
        number
    '''
    
    def test_arg_divisible_by_three(self):
        ''' 
            Test whether a number passed in as an argument
            to the function is divisible by three
        '''
        self.assertEqual(fizz_buzz(9), 'Fizz', msg="Argument expects three or a multiple of three")
        
    def test_arg_divisble_by_five(self):
        '''
            Test whether the number passed in as an argument to
            the function is diivisble by five
        '''
        self.assertEqual(fizz_buzz(25), 'Buzz', msg="Argument expects five or a multiple of five")
        
    def test_arg_divisible_by_three_and_five(self):
        '''
            Test whether the argument passed to the function
            is divisible by both three and five            
        '''
        self.assertEqual(fizz_buzz(15), 'FizzBuzz', msg="Argument should me divisible by both three and five")
        
    def test_func_return_original_arg(self):
        '''
            Test whether the original argument passed is returned as
            the result of the function call if the argument is neither 
            divisible by 3, 5 or 15(3*5)
        '''
        self.assertEqual(fizz_buzz(41), 41, msg="Function should return original argument if the argument is not divisible by either 3, 5 or 15")
        
    def test_no_arg_given(self):
        '''
            Test for case where function is called without any argument
        '''
        with self.assertRaises(TypeError):
            fizz_buzz()
            
    def test_string_argument_given(self):
        '''
            Test whether string value is passed as an argument
        '''
        with self.assertRaises(TypeError):
            fizz_buzz('buzz_fizz')
            
    def test_wrong_logic_for_fizz(self):
        '''
            Test whether function returns "fizz" when it's not
            supposed to
        '''
        self.assertNotEqual(fizz_buzz(15), 'Fizz', msg="Funtion should only return 'Fizz' when it is passed an argument that is a multiple of three but not a multiple of five")
        
    def test_wrong_logic_for_buzz(self):
        '''
            Test whether function returns "Buzz" when it's not supposed to
        '''
        self.assertNotEqual(fizz_buzz(15), 'Buzz', msg="Function should only return 'Buzz' when it's given an argument that is a multiple of 5")
        
    def test_wrong_logic_for_fizz_buzz(self):
        '''
            Test whether function return 'FizzBuzz' when it's not supposed to
        '''
        self.assertNotEqual(fizz_buzz(15), 'Fizz', msg="Function should return 'FizzBuzz' when given an argument that is a a multiple of both 3 and five")
        self.assertNotEqual(fizz_buzz(15), 'Buzz', msg="Function should return 'FizzBuzz' when given an argument that is a multiple of both three and five")   
    
    
    def test_list_arg_passed(self):
        '''
            Tests whether the function was passed a list argument
        '''
        with self.assertRaises(TypeError):
            arguments = [5, 5, 3, 9, 2, 1, 1, 6]
            fizz_buzz(arguments)
    
if __name__ == '__main__':
    unittest.main()