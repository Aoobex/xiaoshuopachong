# coding:utf-8
from soup import makesoup
from find_download_url import find_download_url
from Request_py import geturl_and_request
from get_start_end import getlastchap, savelatestchap
from Downloadtext import downloadtext

url = input('输入小说网址:')

returnList = geturl_and_request(url)

book_id = returnList['bookid']
response = returnList['response']

soup, returnList['booktitle'] = makesoup(response.text)

downloadList = find_download_url(soup, book_id)

start = getlastchap(returnList)

end = downloadtext(downloadList, start, returnList['booktitle'])

savelatestchap(end,returnList)

'''flag = 0
while(flag == 0):
    try:
        r = requests.get(url)
        flag = 1
    except requests.exceptions.RequestException as e:
        print("连接失败，重试")
soup = BeautifulSoup(r.text,'html.parser')      #得到的目录列表
for x in soup.find_all('a',href = re.compile('3319')):
    print(x)
for x in soup.findAll('a'):             #遍历目录
    if('/3319/' in x['href']):           #只对属于本书的目录的地址进行请求
        flag = 0
        url_ = 'https://www.biquge7.com/'+x['href']         #请求这一章的url
        while(flag == 0):
            try:
                r_ = requests.get(url_)
                flag = 1
            except requests.exceptions.RequestException as e:
                print("连接失败，重试")
        soup_ = BeautifulSoup(r_.text,'html.parser')
        texts = soup_.find('div',id = 'chaptercontent')
        text_name = '星空彼岸' + '.txt'
        neirong = texts.text.strip().split()        
        with open(text_name,'a',encoding='utf-8') as f:
            f.write(x.text)
            f.write('\n'*2)
            f.write('\n'.join(neirong))
            f.write('\n')
        print(x.text,'完成')'''
