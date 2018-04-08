import pytest

@pytest.yield_fixture()
def setup():
    print("Setup method...")
    yield
    print("Teardown method...")

def test_m1(setup):
    print("Running test method 1.")

def test_m2():
    print("Running test method 2.")
