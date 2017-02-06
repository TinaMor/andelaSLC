import unittest
from primes import prime_numbers

class prime_number_test(unittest.TestCase):

    def input_is_numeric(self):
        with self.assertRaises(ValueError, msg='Allow only numeric input'):
            prime_numbers(5)

    def test_it_does_not_accept_strings(self):
        with self.assertRaises(ValueError) as context:
            prime_numbers("One")
            self.assertEqual ("The provided input is not an integer.", context.exception.message, "Invalid input of type string not allowed")

    def test_if_input_is_less_than_zero(self):
        with self.assertRaises(ValueError, msg='Allow only positive numbers'):
            prime_numbers(-1)

    def test_if_output_is_list(self):
        result = prime_numbers(5)
        self.assertIsInstance(prime_numbers(5), list, msg="Output must be of type list")
    
    def prime_btwn_1_5(self):
        result = prime_numbers(5)
        self.assertEqual(result, [2, 3, 5], msg='It should produce a list of prime numbers between 1 and 5, (5 inclusive)')

    def output_for_0_is_empty_list(self):
        result = prime_numbers(0)
        self.assertEqual(result, [0], msg='It should produce an empty list')

    def output_for_1_is_empty_list(self):
        result = prime_numbers(0)
        self.assertEqual(result, [1], msg='It should produce an empty list')

    def check_one_is_not_a_prime_number(self):
        result = prime_numbers(1)
        self.assertEqual(result, [1], msg='1 is not a prime number')

if __name__ == '__main__':
  unittest.main()