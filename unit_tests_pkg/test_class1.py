import unittest
import unit_tests_pkg.test_case_demo


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("*#" * 30)
        print("class 1 -> class level setup")
        print("*#" * 30)

    def setUp(self):
        print("Class 1 -> setup")

    def test_class_1_method_A(self):
        print("Running class 1 -> method A")

    def test_class_1_method_B(self):
        print("Running class 1 -> Method B")

    def tearDown(self):
        print("Class 1-> tear down")

    @classmethod
    def tearDownClass(cls) -> None:
        print("*#" * 30)
        print("class 1 -> class level tear down")
        print("*#" * 30)

    if __name__ == '__main__':
        unittest.main(verbosity=3)
