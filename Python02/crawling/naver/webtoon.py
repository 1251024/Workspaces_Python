# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json

#■ 웹툰 제목 가져오기

resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=')
#post 가져올땐 .post
#print(resp)# 응답코드만 가져옴
soup = BeautifulSoup(resp.text, 'html.parser') #실제 텍스트 파일가져오는거

webtoons = soup.find('ul', {'class':'img_list'})
#print(webtoons)

dl = webtoons.select('dl')
#print(dl[0])

'''
for a in dl:
    title = a.find('a').text
    #print(title)
    star = a.find('strong').text
    #print(star)
    print('{} [{}]'.format(title, star))
'''

lst = list()

for chd in dl:
    title = chd.find('a')['title']
    star = chd.find('strong').text
    #print('{} [{}]'.format(title, star))
    
    tmp = {}    #{} 는 셋 or 딕셔너리
    tmp['title'] = title
    tmp['star'] = star
    lst.append(tmp)
    
'''
for i in lst:
    print(i)
'''

# print(lst) #k : v 형태로 바뀜

res = {}
res['webtoons'] = lst
# print(res) # json으로 넣어짐

res_json = json.dumps(res, ensure_ascii=False)
#json 객체가 됨
print(res_json)

with open('webtoons.json', 'w', encoding='utf=8') as f:
    f.write(res_json)