import urllib.request
import json


clientId = '6T78nDxsjCJmIQUkcVCB'
clientSecret = 'HLBS9VQ2Yk'

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-client-Id",clientId)
    req.add_header("X-Naver-client-Secret",clientSecret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except:
        return None
def getNaverSearch(node, srcText, start, display):
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    base = "https://openapi.naver.com/v1/search"
    node = "/news.json"
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(
        srcText),start, display)
    url = base+node+parameters

    responseDecode = getRequestUrl(url)
    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode) #loads() : JSON 문자열을 Python 객체로 변환
    
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    originallink = post['originallink']
    link = post['link']
    pubDate = post['pubDate']
    jsonResult.append({'cnt':cnt, 'title':title,'description':description,
                       'originallink': originallink,'link':link, 'pubDate':pubDate})
    return

node = 'news'
srcText = '선거'
cnt = 0
jsonResult = []

jsonResponse = getNaverSearch(node, srcText, 1, 100) 

# print(jsonResponse)
# print(jsonResponse['total'])
total = jsonResponse['total']
while((jsonResponse!=None) and (jsonResponse['display']!=0)):
    for post in jsonResponse['items']:
        cnt +=1
        getPostData(post, jsonResult, cnt)
    start = jsonResponse['start'] + jsonResponse['display']
    jsonResponse = getNaverSearch(node,srcText,start,10)
print('전체 검색 :%d 건'% total)
print('가져온 데이터 : %d 건'%(cnt))

with open('%s_naver_%s.json'%(srcText,node),'w',encoding='utf-8-sig')as outfile:
    jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,ensure_ascii=False) # json 객체로 변환
    outfile.write(jsonFile)