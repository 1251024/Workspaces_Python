# tuple : ()
# 수정 불가능한 list

# 생성자
a = tuple()
print(a)
# 튜플 객체는 어펜드 속성이 없다
# a.append(1)
# print(a)

b = tuple([1, 2, '3'])
print(b)

# () 사용
c = (1, 2, 3, 4, 5)
print(c)
# c[1] = 'two'
# print(c)
# 튜플객체는 아이템에 접근하는것을 지원하지 않는다.
# 추가도 안되고 수정도 안된다.

d = tuple(range(3, 6))
print(d)
print(c + d)

# tuple을 list로
e = list(d)
print(e)
e.append(6)
print(e)

# list를 tuple로
f = tuple(e)
print(f)
# f.append(6)
# print(f)

# unpacking ->값을 하나하나 따로따로 사용할 때
g, h, i, j = f
print(g)
print(h)
print(i)
print(j)

# 몇개 들어있는지 확실히 알아야 언패킹 가능
# too many values to unpack (expected 3)

# 파이썬의 list도 순서, 중복 가능
