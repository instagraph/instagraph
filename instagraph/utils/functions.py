import requests


def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text


def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})
