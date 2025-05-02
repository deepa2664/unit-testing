import unittest

class TestPositive(unittest.TestCase):
    
    def test_fun(self):
        # Passing test: comparing identical strings
        self.assertEqual("hello", "hello", "Both values are equal.")

if __name__ == '__main__':
    unittest.main()
