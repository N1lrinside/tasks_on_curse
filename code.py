import requests
import re
from art import tprint
from typing import List
def download_url(url: str) -> None:
    print('Downloading ' + url)
    response = requests.get(url=url)
    if response.status_code == 200: #если все успешно, то записываем html в файл
        with open('../Project/url.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
    else:
        print('Error downloading ' + url)

def search_number_phone_on_url(name_url: str) -> List[str]:
    print('Searching numbers')
    with open(name_url, 'r', encoding='utf-8') as f: #открытие файла для работы с ним
        html_code = f.read()
    number=re.findall(r'[^0-9]\+?[78]{1}[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}\b',html_code) # через регулярки находим корректные номера
    change_to_format=list(map(lambda x: re.sub(r'^7','8',re.sub(r'[^0-9]','',x)),number))
    print('Recognized numbers:',end=' ')
    if change_to_format:
        return (dict.fromkeys(change_to_format)) # возвращаем уникальные номера
    else:
        print('No numbers found')

def main() -> None:
    try:
        tprint('Search_numberphone_on_site',font='big') #красивое название :)
        url_input = input("Enter the URL: ")
        download_url(url_input)
        print(*search_number_phone_on_url('url.html'),sep=', ') # Выводит строку с корректными номерам
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()