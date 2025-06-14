import json, sys
from llamacpp_client.client import Client


def health():
    client = Client("http://127.0.1:8080")
    resp = client.health()
    print(resp.status_code, resp.json())


if __name__ == "__main__":
    health()