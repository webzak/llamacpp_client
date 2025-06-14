import sys
from llamacpp_client.client import Client, streamed
from llamacpp_client.models import Completions


def completions():
    client = Client("http://127.0.0.1:8080")
    req = Completions(
        prompt = "Write a function in go language that sums up two integers in go language /no_think",
        n_predict=90,
        stream=True
    )
    resp = client.completions(req)
    print(resp.status_code)
    if resp.status_code != 200:
        print("Error:", resp.json())
        return
    for data in streamed(resp):
        sys.stdout.write(data["content"])
    print("")

if __name__ == "__main__":
    completions()