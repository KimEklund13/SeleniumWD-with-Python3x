import unittest


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("***" * 30)
        print("I will run only once before all tests")
        print("***" * 30)

    def setUp(self) -> None:
        print("I will run once before every test")

    def test_methodA(self):
        print("running methodA")

    def test_methodB(self):
        print("running methodB")

    def tearDown(self) -> None:
        print("I will run after each test")

    @classmethod
    def tearDownClass(cls) -> None:
        print("***" * 30)
        print("I'm done running all the tests")
        print("***" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)