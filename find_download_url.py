# name:Dr.Luo
from bs4 import BeautifulSoup
import re


def find_download_url(soup, book_id):
    returnList = []
    temp = 1
    # 查找所有a标签，且属性值href需要含有书本的id
    for url in soup.find_all('a', href=re.compile(book_id)):
        if temp == 1:
            temp = 0
            continue
        returnList.append(['https://www.bige7.com/' + url['href'], url.get_text()])
    return returnList
