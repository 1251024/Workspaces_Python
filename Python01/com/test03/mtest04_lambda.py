# lambda 파라미터 : 리턴될 값
from unittest.test.testmock.testpatch import function

hap01 = lambda a, b: a + b
print(hap01(10, 20))

gob = lambda a, b: a * b
print(gob(10, 20))

hap02 = lambda a, b, c: a + b + c
print(hap02(10, 20, 30))

a = [(1, 'one', 9), (2, 'two', 8), (3, 'three', 7), (4, 'four', 6)]
#a.sort(key=lambda a:a[1]) # 1번지 기준으로 정렬 됨(문자열 영어기준으로 f o t t)
a.sort(key=lambda a:a[2]) # 2번지 기준으로 6 7 8 9로 정렬
print(a)


# min01 = lambda x, y: x if x < y else y
#print(min01(11, 22))
min01 = (lambda x, y: x if x < y else y)(11, 22)
# 조건 : if x < y (x가 y보다 작으면)
# 참일때 x, 거짓일때 y
# 제어문(for, if)을 한 줄로 쓸 수 있다.
#if x < y:
#    x
#else : 
#    y
# 위와 같음    
print(min01)

max01 = (lambda x, y: x if x > y else y)(33, 44)
print(max01)


#람다식은 익명함수
#람다가 중첩되어 ㅣㅇㅆ으면
# 파라미터는 x하나, (lambda newx: x + newx)도 함수 하나
#b에 100, newx에 90
b = lambda x:(lambda newx: x + newx)
print(b(100)(90))
# 파라미터 하나가 들어오면
# : 명령해서 리턴해줄거야(이번엔 람다식을 리턴)

#풀어서 쓴다면 ...
# c = lambda newx : 100 + newx
# b(100) = lambda newx : 100 + newx     <-람다식
c = b(100)
print(c)
# d = 100 + 90
d = c(90)
print(d)


# 1 ~ 100 사이에서 5의 배수 출력
e = lambda x: bool(x % 5) # 5로 나누어 떨어지면 False, 그외에 True 
#print(e(9)) 
#숫자가 0이면거짓, 0이 아니면 참
#(){}[] 비어있으면 거짓

five = [i for i in range(1, 100)if not e(i)]
#[]리스트
# for i in range(1, 100): 1부터 100전꺄지 반복할거야
# 만일 i가 not e(i), 5로 나눈 나머지가 0일때 , 0이면 true i면 false
print(five)


# None == Null (None과 Null은 비슷하다)
f = lambda x: x if (x % 5 != 0) else None
res = [i for i in range(1,100) if not f(i)]
print(res)

#if (x % 5 != 0)이 조건이 참이면 x, 거짓이면 None
# f(i)에는 none아니면 1,2,3..숫자가 들어가는데 / none만 true, 나머지는 false
# 참인 애들만 가지고와서 리스트로 만들자


#합쳐보자
result = [i for i in range(1, 100) if not (lambda x: x if (x % 5 != 0) else None)(i)]
print(result)
