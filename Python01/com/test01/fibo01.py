# 0 1 1 2 3 5 8 13 21 34 55 ...

n = input('level : ')
a, b = 0, 1
i = 0
while i < int(n): # i < int(n): 조건, 해당 조건이 참일때까지 반복
    print(a, end=' ')
    a, b = b, a+b #a = b, b = a + b 이렇게 대입해주는 것
    i += 1 #종료되는 조건

