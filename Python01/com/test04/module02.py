# cmd에서 가상환경 만들기(basic이란 가상환경만들때마다 한번만)
# cd /
# cd venvs
# .\basic\Scripts\activate.bat
# pip install numpy            -> 수치해석
# pip install matplotlib       -> 그래프 (시각화)

# import <module_name> as <alias>
import numpy as np
import matplotlib.pyplot as plt
import random
# np와 plt는 암묵적 이름

def plt01():
    x =np.arange(0, 11)
    y = x
    # print(x)
    
    plt.plot(x, y)#x,y로 뭐만들거야
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    #legend : 범례(그래프 위에 쪼꼬만한거)
    plt.legend(['y = x'])
    
    plt.show()
    
    
plt01()

#[ 0  1  2  3  4  5  6  7  8  9 10]
# numpy가 가지고 있는 배열(array)


def plt02():
    y = [random.randint(0, 10) for _ in range(10)]
    # _로 쓰면 값을 지정안하고 버리는 값이야 / 랜덤으로 10번 반복하는데 특별히 어디서 사용 안하고 리스트에 담아서 사용할거야
    x = range(10)
    
    plt.bar(x, y)
    
    # 축 간격 설정
    plt.xticks(range(11))
    plt.yticks(range(11))
    
    plt.show()
    
    
plt02()


def plt03():
    data = [random.randint(100, 1000) for _ in range(4)]
    
    plt.pie(data)
    
    category = ['first', 'second', 'third', 'fourth']
    plt.legend(category)
    
    plt.show()
    
plt03()