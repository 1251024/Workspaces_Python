# -*- coding:utf-8 -*-

file = open('test01.txt', 'w') # open : 파일 열거야, 'w' 모드이고 여러개 모드를 합칠 수 있음
file.write('Hello, world!')
file.close()

# 같은 경로 파일에 test01.txt 저장됨
# 새로고침하면 확인 할 수 있음

'''
r : 읽기
w : 쓰기 (기존 내용 덮어쓰기)
a : 쓰기 (기존 내용 이어서 쓰기)
x : 새로운 파일 만들어서 쓰기 (이미 파일이 있으면 에러)
t / b : text / binary (default : t)
'''