import pytest


@pytest.fixture()
def setUp():
    print(" ----- > Running pre-test setup")
    yield
    print(" ------ > Running post-test down")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print(" ----- > Running pre-module setup")
    if browser == "firefox":
        value = 10
        print("running tests on firefox")
    else:
        print("running tests on chrome")
        value = 20
    if request.cls is not None:
        request.cls.value = value
    yield value
    print(" ------ > Running post-module tear down")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")