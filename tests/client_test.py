import pytest
from llamacpp_client.client import Client
from unittest.mock import patch
import requests

class TestClient:

    def setup_method(self):
        self.url = "http://127.0.0.1:8080"
        self.client = Client(self.url)


    def teardown_method(self):
        pass

    def set_mock_response(self, mocker, code, data):
        mock_response = mocker.return_value
        mock_response.status_code = code
        mock_response.json.return_value = data

    @patch('requests.get')
    def test_api_key(self, mocker):

        self.set_mock_response(mocker, 200, {"status": "OK"})

        apikey = "apikey"
        client = Client(self.url, apikey)

        resp = client.health()

        assert resp.status_code == 200
        assert resp.json() == {"status": "OK"}

        mocker.assert_called_once_with(
            self.url + "/health", params={},
            headers={"Authorization": "Bearer " + apikey},
            stream=False
        )


    @patch('requests.get')
    def test_health(self, mocker):

        self.set_mock_response(mocker, 200, {"status": "OK"})

        response = self.client.health()
        print(f"response: {response}")

        assert response.status_code == 200
        assert response.json() == {"status": "OK"}

        mocker.assert_called_once_with(
            self.url + "/health", params={},
            headers={},
            stream=False
        )