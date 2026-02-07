import requests


class ReadeckError(Exception):
    pass


class ReadeckClient:
    def __init__(self, api_url: str, api_token: str):
        self.api_url = api_url
        self.api_token = api_token

    def create_bookmark(self, url: str) -> None:
        response = requests.post(
            f"{self.api_url}/api/bookmarks",
            json={"url": url},
            headers={"Authorization": f"Bearer {self.api_token}"},
            timeout=30,
        )
        if not response.ok:
            raise ReadeckError(
                f"Readeck API returned {response.status_code}: {response.text}"
            )
