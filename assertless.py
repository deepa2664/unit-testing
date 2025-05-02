# test suite 
import unittest 

class TestStringMethods(unittest.TestCase): 
	
	# negative test function to test if 
	# values1 is less than value2 
	def test_negativeForLess(self): 
		first = 6
		second = 5
		
		# error message in case if test case got failed 
		message = "first value is not less that second value."
		
		# assert function() to check if values1 is 
		# less than value2 
		self.assertLess(first, second, message) 

# main for function call 
if __name__ == '__main__': 
	unittest.main()
