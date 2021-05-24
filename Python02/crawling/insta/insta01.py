# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

tag = input('search tags : ')
url = 'https://www.instagram.com/explore/tags/' + tag

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

print(soup.find('div', {'class', 'KL4Bh'}))
# 인스타는 ajax로 비동기 통신 함
# 인스타가 응답되어진 후 ajax로 가지고온 데이터들은 못가져옴 -> 셀레니움이 필요