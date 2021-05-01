'''
'''
__author__ = 'Boda Zsolt'

import sys
import requests
from requests import Response
from typing import Dict
from pprint import pprint

API_KEY: str = 'RGAPI-3ce3c65a-f561-4dc5-aa50-4b01eb2cd6f0'
USERNAME: str = 'GTDiablo'
REGION: str = 'eun1'
VERSION: int = 4
API_URL: str = 'https://{region}.api.riotgames.com/lol/summoner/v{version}/summoners/by-name/{names}'

def main() -> int:
    api_url: str = API_URL.format(region=REGION, version=VERSION, names=USERNAME)
    payload: Dict[str, str] = {'api_key': API_KEY}
    response: Response = requests.get(api_url, params=payload)
    pprint(response.json())
    return 0

if __name__ == '__main__':
    sys.exit(main())