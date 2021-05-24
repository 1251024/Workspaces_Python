import random

def lotto():
    result = set()
    
    # len() : length -> 객체의 길이를 리턴 (set같은 하나씩 가져올 수 있는 것들의 길이를 리턴)
    while len(result) <= 6:
        ran = random.randint(1, 45)
        result.add(ran)
    lst = sorted(result)
    print(lst)

if __name__ == '__main__':
    lotto()
    