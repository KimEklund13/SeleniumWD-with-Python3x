import pytest


@pytest.fixture()
def setUp():
    print("Once before every method")


def test_demo1_methodA(setUp):
    print("Running method A")


def test_demo1_methodB(setUp):
    print("Running method B")
