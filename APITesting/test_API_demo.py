import pytest
import requests
  
@pytest.mark.usefixtures("argSetup", "setup")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.a = 3
        self.b = 5

    def test_get_API(self):
        response = 200
        print("Running get API test.")
        test_url = 'http://ip.jsontest.com'
        resp = requests.get(test_url)
        print(resp.text)
        assert resp.status_code == response

    def test_post_API(self):
        response = 200
        print("Running post API test.")
        test_url = 'http://ip.jsontest.com'
        headers = {'Content-type': 'application/json'}
        payload = {'ip': '10.35.35.203'}
        resp = requests.post(test_url, data=payload, headers=headers)
        print(resp.text)
        assert resp.status_code == response
