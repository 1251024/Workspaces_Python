# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
#urllib 는 요청해서 '응답받는 역할'을 해줌

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
print(resp)

'''
■ 네이버 영화 제목,별점 크롤링하는 법!

● beautifulsoup4는? (스크래핑하기 좋은 툴)
크롤링은 다 가져오는거
스크래핑은 내가 원하는 부분만 가져오는 것

● cmd에서 beautifulsoup4 설치
'''



soup = BeautifulSoup(resp, 'html.parser')
# print(soup)
# f12 했을때 코드 가져온것을
# Python’s html.parser : html로 파싱해준 것
# 넘어온것은 BeautifulSoup객체(스트링 아님, dom탐색 가능 ->soup.***)

#lst_dsc가져오기
movies = soup.find_all('dl', class_='lst_dsc')
# print(movies[1])

for movie in movies:
    # 영화제목 [평점]
    # ex) 스파이럴 [9.83]
    title = movie.find('a').text
    #print(title)
    star = movie.find('span', class_='num').text
    print('{} [{}]'.format(title, star))
