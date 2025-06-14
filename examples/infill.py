import json, sys
from llamacpp_client.client import Client
from llamacpp_client.models import Infill



def infill():
    client = Client("http://127.0.0.1:8080")
    req = Infill(
        prompt = "",
        n_predict=300,
        stream=False,
        input_prefix=
        """
        func add(int a, b) int {
            return a + b\n
        }
        """,
        input_suffix="""
        func sub(int a, b) int {
            return a - b
        }
        """
    )

    resp = client.infill(req)
    print(resp.status_code)
    result = resp.json()
    print(json.dumps(result, indent=4))
    print(result["content"])

if __name__ == "__main__":
    infill()