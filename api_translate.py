import requests

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

API_KEY = 'trnsl.1.1.20221226T141018Z.6c3102b63a900a71.6e852bcc630d9139caa8b1140051e5c15e9aa442'

word_to_translate = 'Hello'

params = dict(key=API_KEY, text=word_to_translate, lang='en-pt')

res = requests.get(url, params=params)

json = res.json()

if res:
    print(json['text'][0])
else:
    print('Response Failed')
