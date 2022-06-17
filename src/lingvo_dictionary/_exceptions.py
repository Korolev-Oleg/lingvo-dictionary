from requests import Response


class LingvoException(Exception):
    def __init__(self, response: Response):
        super().__init__(f"\n status_code <{response.status_code}> {response.url}\n"
                         f" {response.json()}")
