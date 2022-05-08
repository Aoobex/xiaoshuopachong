# name:Dr.Luo
import requests
from bs4 import BeautifulSoup


def downloadtext(downloadList, start, booktitle):
    length = len(downloadList)
    for i in range(start, length):
        text_url_response = requests.get(downloadList[i][0])
        text_url_response_soup = BeautifulSoup(text_url_response.text, 'html.parser')
        texts = text_url_response_soup.find('div', id='chaptercontent')
        text = texts.text.split()
        title = downloadList[i][1]
        with open(booktitle + '.txt', 'a', encoding='utf-8') as f:
            f.write(title)
            f.write('\n'*2)
            f.write('\n'.join(text))
            f.write('\n')
        print(title + '完成')
    return length