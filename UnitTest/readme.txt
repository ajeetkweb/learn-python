 Basics of Unit Testing in Python =======

1. Import the unittest module.

2. Create a test case class that inherits from unittest.TestCase.

3. Write test methods (method names must start with test_).

4. Use assertions to verify behavior.

5. Run the tests using unittest.main().


 Running Tests :

  python test_calculator.py



Common Assertions : 

Assertion Method	                 Purpose

assertEqual(a, b)	                 a == b

assertNotEqual(a, b)	             a != b

assertTrue(x)	                     bool(x) is True

assertFalse(x)	                     bool(x) is False

assertIsNone(x)	                     x is None

assertIsInstance(x, type)	         isinstance(x, type)

assertRaises(Error, func)	         Error is raised by func()