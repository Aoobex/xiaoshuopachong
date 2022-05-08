# name:Dr.Luo
from bs4 import BeautifulSoup


def makesoup(response_text):
    soup = BeautifulSoup(response_text,'html.parser')
    return [soup,soup.title.get_text()]