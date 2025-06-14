import json, sys
from llamacpp_client.client import Client
from llamacpp_client.models import Detokenize

def detokenize():
    client = Client("http://127.0.0.1:8080")
    req = Detokenize(
        tokens = [128000, 606, 1403, 2380, 3116, 4330]
    )
    resp = client.detokeninze(req)
    print(resp.status_code)
    result = resp.json()
    print(json.dumps(result))


if __name__ == "__main__":
    detokenize()