# list : []

# 생성자
a = list()
print(a)
a.append(1)
print(a)
# 배열로 들어가짐
a.append('one')
print(a)
# 1번지 내용을 바꿀 수 있음
a[1] = 'two'
print(a)
#리스트의 인덱스가 할당되지 않음(list 사이즈보다 더 큰곳으로 넣어주세요)
# a[2] = 3
# print(a)

# []사용
b = [1, 2, 3, 4, 5]
print(b)
print(b[0] + b[4])

# 거꾸로 출력
b.reverse()
print(b)

# 정렬
b.sort()
print(b)

# 중첩
c = ['a', 'b', 'c', ['d', 'e', 'f']]
print(c)

print(c[3][2])

print(b + c)
