# -*- coding:utf-8 -*-

# 스타벅스 지역검색 시도리스트 검색
#    __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post",
#    if ( sido == "17") //세종시는 구군이 없어 바로 검색한다.
#    __ajaxCall("/store/getSidoList.do", {}, true, "json", "post",
# https://www.starbucks.co.kr/

# requests : 내장모델보다 사용하기 쉬워서 사용 

import requests
import json
from Tools.scripts.dutree import store


# 시도 리스트
def getSiDo():
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    resp = requests.post(url) # 시도 list 응답받을 객체 만들기
    #print(resp)
    #print(resp.text) #json으로 응답되는거 확인 가능 // .text: string / .json(): json객체로 응답됨
    #print(resp.json()['list'][0]) # list 확인할 수 있음
    
    #list 가져오기
    sido_json = resp.json()['list']
    
    # 필요한 부분만 list로 만들기('sido_cd': '01', 'sido_nm': '서울' 가져올 예정)
    sido_code = list(map(lambda x: x['sido_cd'], sido_json)) # map 함수는 sido_json 컬렉션 list에 적용시켜서 결과를 리턴하고 그 결과값이 map객체라서 map객체를 list로 뽑아냄
    # print(sido_code)
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    # print(sido_name)
    
    # 딕셔너리로 바꾸기
    sido_dict = dict(zip(sido_code, sido_name)) #dict : 딕셔너리 생성자 / k:v형태로 만들기 (딕셔너리 타입은 immutable한 키(key)와 mutable한 값(value)으로 맵핑되어 있는 순서가 없는 집합입니다.)
    # print(zip(sido_code, sido_name)) #zip : 리스트 두개를 하나로 묶어줌 = code와 name을 하나씩 묶어줌 (순서대로)
    # print(sido_dict)
    return sido_dict
    
# 구군 리스트
def getGuGun(sido_code):
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    resp = requests.post(url, data={'sido_cd': sido_code}) # 시도 코드에 맞는 구군list 응답받을 객체 만들기
    # print(resp.json())
    gugun_json = resp.json()['list'] # 구군 리스트 가져오기
    
    # 필요한 부분만 list로 만들어서 dict객체로 만들기
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_json)), list(map(lambda x: x['gugun_nm'], gugun_json))))
    # print(gugun_dict)
    return gugun_dict
    
    
# 새로고침 후 스토어 - 지역검색 - 서울 누르고 개발자 도구f12 누르고 강남구 누른다음 개발자도구 네트워크탭에 getstore의 요청, 응답탭 확인      
def getStore(sido_code='', gugun_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url, data={
                                    'ins_lat' : '37.5009759',
                                    'ins_lng':'127.03735019999999',
                                    'p_sido_cd': sido_code,
                                    'p_gugun_cd': gugun_code,
                                    'in_biz_cd': '',
                                    'set_date': ''
                                    })
    # print(resp.json()['list'][0])
    store_json = resp.json()['list']

    store_list = list() #list 담을거 만들기
    count = 0
    
    #s_name, tel, doro_address, lat, lot 가져오기
    for store in store_json:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        store_list.append(store_dict)
        count += 1

    store_tmp = dict()
    store_tmp['store_list'] = store_list
    store_tmp['count'] = count
    result_json = json.dumps(store_tmp, ensure_ascii=False)
    #print(result_json)
    return result_json
    
    
if __name__ == '__main__':
    #getSiDo()
    print(getSiDo()) #sido list 출력
    sido = input('시도 코드를 입력해 주세요 : ') 
    if sido == '17':    # 세종시는 구군이 없어 바로 검색 된다.
        print(getStore(sido_code=17))
    else:
        # getGuGun(sido)
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해주세요 : ')
        print(getStore(gugun_code=gugun))
    