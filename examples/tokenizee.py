import json, sys
from llamacpp_client.client import Client
from llamacpp_client.models import Tokenize


def tokenize():
    client = Client("http://127.0.0.1:8080")
    req = Tokenize(
        content = "one two three four five",
        add_special=False,
        with_pieces=True
    )
    resp = client.tokeninze(req)
    print(resp.status_code)

    result = resp.json()
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    tokenize()