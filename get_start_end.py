# name:Dr.Luo

def getlastchap(returnList):
    try:
        with open(returnList['bookid']+'.txt', 'r', encoding='utf-8') as f:
            result = f.read()
            return int(result)
    except:
        open(returnList['bookid']+'.txt', 'x', encoding='utf-8')
        return 0

def savelatestchap(chap,returnList):
    with open(returnList['bookid']+'.txt', 'w', encoding='utf-8') as f:
        f.write(str(chap))
        f.close()