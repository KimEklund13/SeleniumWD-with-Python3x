import pytest


@pytest.fixture()
def setUp():
    print(" ----- > Running pre-test setup")
    yield
    print(" ------ > Running post-test down")


@pytest.fixture(scope="module")
def oneTimeSetUp(browser, osType):
    print(" ----- > Running pre-module setup")
    if browser == "firefox":
        print("running tests on firefox")
    else:
        print("running tests on chrome")
    yield
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