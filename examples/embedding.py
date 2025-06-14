import json, sys
from llamacpp_client.client import Client
from llamacpp_client.models import Embedding

def embedding():
    client = Client("http://127.0.0.1:8080")
    req = Embedding (
        content = "one two three four five",
    )
    resp = client.embedding(req)
    print(resp.status_code)

    result = resp.json()
    print(json.dumps(result))


if __name__ == "__main__":
    embedding()