# name:Dr.Luo
'''对url响应，并获取本书id'''

import requests


def geturl_and_request(url):
    returnList = {}
    request_ok_flag = False
    while not request_ok_flag:
        try:
            response = requests.get(url)
            request_ok_flag = True
        except:
            print('连接服务器失败，重试中')
    returnList['response'] = response

    bookid = ''
    find_flag = False
    length = len(url)
    for i in range(length - 1, -1, -1):
        try:
            int(url[i])
            find_flag = True
            bookid = url[i] + bookid
        except:
            if find_flag is False:
                continue
            if find_flag is True:
                break
    returnList['bookid'] = bookid

    return returnList
