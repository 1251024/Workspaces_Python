# 산술연산
a = 21
b = 2
print(a + b)    # 더하기
print(a - b)    # 빼기
print(a * b)    # 곱하기
print(a ** b)   # a의 b승(제곱)
print(a / b)    # 나누기
print(a // b)   # 몫 (floor division)
print(a % b)    # 나머지

# 비교연산 (비교라서 결과는 참 or 거짓으로 출력)
a, b = 5, 3
print(a == b)       # a와 b는 같다       -> 거짓
print(a != b)       # a와 b는 같지 않다  -> 참
print(a > b)        # a는 b보다 크다     -> 참
print(a >= b)       # a보다 같거나 크다  -> 참
print(a is b)       # a는 b다            -> 거짓
print(a is not b)   # a와 b는 같지않다   -> 참

# 범위연산
list01 = list(range(100)) # 0 ~ 99
print(list01)

# [start: end] -> start ~ end-1
# [start: end: step] -> start ~ end-1까지 step만큼씩
print(list01[12: 50])
print(list01[12: 49: 3])


start01 = 'Hello World!'
print(start01[0])
print(start01[0: 5])
print(start01[6: 11])   # 6부터 해당숫자까지
print(start01[6: ])     # 6부터 끝까지

# -1
print(start01[-1])      # 오른쪽 숫자에서부터 거꾸로 찾음
print(start01[-3:])     # 오른쪽 숫자에서부터 끝까지
print(start01[: -1])    # 오른쪽 끝에서 -1전까지
print(start01[:: -1])   # 역순

# in, not in
start02 = [1, 2, 3, 4, 5, 6]
print(3 in start02)     # 참
print(6 not in start02) # 거짓
print(9 not in start02) # 참
