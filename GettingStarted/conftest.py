import pytest
  
@pytest.yield_fixture()
def setup():
    print("Setup method...")
    yield
    print("Teardown method...")

@pytest.yield_fixture()
def argSetup(browser):
    print("Running arg setup method...")
    if browser == 'chrome':
        print("Running tests on chrome")
    else:
        print("Running tests on safari")

    yield
    print("Running arg teardown method...")

def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser options")
    parser.addoption("--os", help="Operating system")

@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def os(request):
    return request.config.getoption("--os")
