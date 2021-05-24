
def func01():
    print('함수 1 입니다.')
    
def func02():
    return '함수 2 입니다.'

def func03():
    return {1: 'a', 2: 'b'}

# main 함수 -> 프로그램 주 진입점
if __name__ == '__main__':
    print('프로그램 시작시 가장 먼저 호출됨!') 
    func01()
    print(func02())
    # func03 함수를 호출하여, 리턴받은 dict에서 b값만 출력!
    print(func03()[2])
    
#__i__는 프로젝트 내부에서만 사용되는 변수, 파이썬 내부에서 만들어놓은 내장 함수


