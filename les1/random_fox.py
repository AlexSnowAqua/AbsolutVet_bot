import requests


def fox():
    url = 'https://randomfox.ca/floof/'
    responce = requests.get(url)
    if responce.status_code:
        data = responce.json()
        return data.get('image')


if __name__ =='__main__':
    fox()

