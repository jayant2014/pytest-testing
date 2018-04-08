import pytest

@pytest.mark.usefixtures("argSetup", "setup")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.a = 3
        self.b = 5

    def test_m1(self):
        sum = 8
        a = 3
        b = 5
        result = a + b
        print("Running test method 1.")
        assert sum == result

    @pytest.mark.xfail(reason="BUG-1000")
    def test_m2(self):
        print("Running test method 2.")
