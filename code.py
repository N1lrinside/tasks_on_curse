import requests
import re
from art import tprint
def download_url(url):
    print('Downloading ' + url)
    response = requests.get(url=url)
    if response.status_code == 200:
        with open('../Project/url.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
def search_number_phone_on_url(name_url):
    print('Searching numbers')
    with open(name_url, 'r', encoding='utf-8') as f:
        html_code = f.read()
    number=re.findall(r'[^0-9]\+?[78]{1}[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}\b',html_code)
    change_to_format=list(map(lambda x: re.sub(r'^7','8',re.sub(r'[^0-9]','',x)),number))
    print('Recognized numbers:',end=' ')
    return list(dict.fromkeys(change_to_format)) # возвращаем уникальные номера
def main():
    try:
        tprint('Search_numberphone_on_site',font='big')
        url_input = input("Enter the URL: ")
        download_url(url_input)
        print(*search_number_phone_on_url('url.html'),sep=', ')
    except Exception as err:
        print(err)
if __name__ == '__main__':
    main()