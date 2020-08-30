#este programa practica el uso del metodo post

import requests
req = requests.get('https://www.youtube.com/')
req.raise_for_status()
with open('youtube.html', 'wb') as fd:
    for chunk in req.iter_content(chunk_size=50000):
        fd.write(chunk)
