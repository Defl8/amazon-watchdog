import requests
from requests import Response


def get_item_page_html(url: str) -> str | None:
    response: Response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        response.raise_for_status()
