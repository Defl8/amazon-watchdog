import requests
from requests import Response

def get_item_page_html(url: str):
    response: Response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return response
    else:
        response.raise_for_status()
