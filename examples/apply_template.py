import json, sys
from llamacpp_client.client import Client
from llamacpp_client.models import ApplyTemplate, Message


def apply_template():
    client = Client("http://127.0.0.1:8080")
    req = ApplyTemplate (
        messages = [
            Message(role = "system", content = "message one"),
            Message(role = "user", content = "message two"),
            Message(role = "assistant", content = "message three"),
        ],
    )
    resp = client.apply_template(req)
    print(resp.status_code)

    result = resp.json()
    print(json.dumps(result))


if __name__ == "__main__":
    apply_template()