def mysum(x, y):
    return 2 * x + y

if __name__ == '__main__':
    print(mysum(2, 3))
    
    print((lambda x, y: 2 * x + y)(2, 3))
    #(lambda x, y: 2 * x + y) 는 식, 파라미터 2개
    #mysum=(lambda x, y: 2 * x + y)
    