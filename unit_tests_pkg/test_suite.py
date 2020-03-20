import unittest
from unit_tests_pkg.test_class1 import TestClass1
from unit_tests_pkg.test_case_demo import TestCaseDemo

# get all tests from TestClass1 and TestCaseDemo
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)

# create a test suite combining both classes
suite = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(suite)