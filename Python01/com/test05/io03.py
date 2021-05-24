# -*- coding:utf-8 -*-

with open('test01.txt', 'r') as file:
    a = file.read()
    print(a)
    
# with open() as는 file변수에 담아주는데, with open이 변수의 클로즈를 자동으로 해줌