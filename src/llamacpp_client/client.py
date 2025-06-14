import pydantic
import requests, json
from typing import Any

from .exceptions import InvalidRequest
from . import models


class Client():
    """
    The client for llama.cpp server api
    """
    def __init__(self, url: str, apikey: str = ""):
        """ construct class by providing url and optionally apikey """
        if not isinstance(url, str):
            raise TypeError("url must be string")
        if not isinstance(apikey, str):
            raise TypeError("apikey must be a string")
        self.url = url
        self.headers = {}
        if len(apikey) > 0:
            self.headers["Authorization"] = "Bearer " + apikey


    def _request(self, method: str, path: str, query: dict = {}, data: dict = {}, stream=False) -> requests.Response:
        """
        execute request for specified path
        """
        if not isinstance(method, str):
            raise TypeError("method must be a string")
        method = method.lower()
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        if not isinstance(query, dict):
            raise TypeError("query must be a dictionary")
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
        resp = None
        if method == "get":
            resp = requests.get(self.url + path, params=query, headers=self.headers.copy(), stream=stream)
        elif method == "post":
            resp = requests.post    (self.url + path, json=data, headers=self.headers.copy(), stream=stream)
        else:
            raise TypeError("invalid request method: " + method)
        resp.raise_for_status()
        return resp


    def health(self) -> requests.Response:
        """
        call the /health route
        """
        return self._request("GET", "/health")


    def completions(self, params: dict[str, Any] | models.Completions) -> requests.Response:
        """
        Completions api
        """
        if isinstance(params, dict):
            try:
                params = models.Completions(**params)
            except pydantic.ValidationError as e:
                raise InvalidRequest(e.errors())
        elif isinstance(params, models.Completions):
            pass
        else:
            raise TypeError(f"invalid type for params: {type(params).__name__}")
        return self._request("POST", "/completions", data=params.model_dump(exclude_none=True), stream=params.stream)


    def infill(self, params: dict[str, Any] | models.Infill) -> requests.Response:
        """
        Completions api
        """
        if isinstance(params, dict):
            try:
                params = models.Infilll(**params)
            except pydantic.ValidationError as e:
                raise InvalidRequest(e.errors())
        elif isinstance(params, models.Infill):
            pass
        else:
            raise TypeError(f"invalid type for params: {type(params).__name__}")
        return self._request("POST", "/infill", data=params.model_dump(exclude_none=True), stream=params.stream)


    def tokeninze(self, params: dict[str, Any] | models.Tokenize) -> requests.Response:
        """
        Tokenize api
        """
        if isinstance(params, dict):
            try:
                params = models.Tokenize(**params)
            except pydantic.ValidationError as e:
                raise InvalidRequest(e.errors())
        elif isinstance(params, models.Tokenize):
            pass
        else:
            raise TypeError(f"invalid type for params: {type(params).__name__}")
        return self._request("POST", "/tokenize", data=params.model_dump(exclude_none=True))

    def detokeninze(self, params: dict[str, Any] | models.Detokenize) -> requests.Response:
        """
        Detokenize api
        """
        if isinstance(params, dict):
            try:
                params = models.Detokenize(**params)
            except pydantic.ValidationError as e:
                raise InvalidRequest(e.errors())
        elif isinstance(params, models.Detokenize):
            pass
        else:
            raise TypeError(f"invalid type for params: {type(params).__name__}")
        return self._request("POST", "/detokenize", data=params.model_dump(exclude_none=True))


    def apply_template(self, params: dict[str, Any] | models.ApplyTemplate) -> requests.Response:
        """
        Apply template api
        """
        if isinstance(params, dict):
            try:
                params = models.ApplyTemplate(**params)
            except pydantic.ValidationError as e:
                raise InvalidRequest(e.errors())
        elif isinstance(params, models.ApplyTemplate):
            pass
        else:
            raise TypeError(f"invalid type for params: {type(params).__name__}")
        return self._request("POST", "/apply-template", data=params.model_dump(exclude_none=True))


    def embedding(self, params: dict[str, Any] | models.Embedding) -> requests.Response:
        """
        Embedding api
        """
        if isinstance(params, dict):
            try:
                params = models.Embedding(**params)
            except pydantic.ValidationError as e:
                raise InvalidRequest(e.errors())
        elif isinstance(params, models.Embedding):
            pass
        else:
            raise TypeError(f"invalid type for params: {type(params).__name__}")
        return self._request("POST", "/embedding", data=params.model_dump(exclude_none=True))


def streamed(resp: requests.Response, skip_errors: bool=False):
    """
    A generator function that processes lines from a requests.Response object,
    extracts JSON data from lines starting with 'data: ', and yields the parsed
    JSON data.
    """
    for line in resp.iter_lines():
        if line:
            try:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    json_string = decoded_line[6:]
                    data = json.loads(json_string)
                    yield data  # Yield the parsed JSON data
            except Exception as e:
                if not skip_errors:
                    print(f"An error occurred while processing line: {line}. Error: {e}")
                pass
