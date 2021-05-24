# -*- coding:utf-8 -*-

import pickle

score = {"name": 'kh', 'kor': 100, 'eng': 60, 'math': 75}
with open('test02.txt', 'wb') as file:
    pickle.dump(score, file)
    #파이썬에 딕셔너리 파이썬객체가 바이너리 형태로 저장

'''
pickling : 객체 -> 파일
unpickling : 파일 -> 객체
'''
