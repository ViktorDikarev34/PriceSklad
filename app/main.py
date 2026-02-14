from pprint import pprint
import requests

from app.config import settings

token = settings.TOKEN

headers = {
    'Authorization': f'Bearer {token}',
    'Accept-Encoding': 'gzip'
}

response = requests.get('https://api.moysklad.ru/api/remap/1.2/entity/processingplan',
                        headers=headers)
pprint(len(response.json()))