# 1. for문을 사용하여 구구단을 출력하는 gugu() 함수를 만들자.
# 2. while문을 사용하여 구구단 중 입력된 단만 출력하는 gugudan(x) 함수를 만들자.
# 3. main함수에서, gugu와 gugudan을 호출하는데, input() 함수를 사용하여 단을 입력하여 호출하자.

def gugu():
    for i in range(2, 10):
        print('<<%d 단>>' % i)
        for j in range(1,10):
            print('%d * %d = %d' % (i, j, i*j))
        print()

def gugudan(x):
    print('<<{}단>>'.format(x))
    i = 1
    while i < 10:
        print('{} * {} = {}'.format(x, i, x*i))
        i += 1

#__i__는 프로젝트 내부에서만 사용되는 변수, 파이썬 내부에서 만들어놓은 내장 함수
if __name__ == '__main__':
    gugu()
    
    dan = input('단을 입력해주세요 : ')
    gugudan(int(dan))
    
