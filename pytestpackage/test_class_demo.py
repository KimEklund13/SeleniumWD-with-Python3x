import pytest
from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    # Fixture to help run the test methods on the class level (only this class)
    # Autouse makes the fixture apply to all the test methods in this class
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")
