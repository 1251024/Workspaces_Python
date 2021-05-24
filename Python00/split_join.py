# split

str01 = 'Hello, World!\nHello, Python!'
print(str01)

arr01 = str01.split(' ') # 공백으로 짜른다
print(arr01)

arr02 = str01.split('\n') # \n으로 짜른다
print(arr02)

arr03 = str01.split(' ', 1) # 공백으로 한번만 짤라주세요
print(arr03)

import re

# 정규식으로 자르기
arr04 = re.split('[\s]|[,]', str01) # 공백과 , 기준으로 짜르겠다.
print(arr04)

# join
arr05 = ['1', '2', '3', '4']
print(arr05)
print('+'.join(arr05))
print(eval('+'.join(arr05)))
