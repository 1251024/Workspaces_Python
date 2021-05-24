subject = ['java', 'javascript', 'python']

for i in subject:
    print(i, end=' ')
else:
    #반복문에서의 else : 반복문이 정상 종료되었을 때 실행됨
    print('재밌다.')

for i in range(1, 100):
    # 1~ end-1(100-1) 까지 실행
    print(i, end=' ')
print()

for i in range(10, 0, -1): #start에서 end까지 (-1은 step) -1씩 증가해라
    print(i, end=' ')
print()

for i in range(1, 10, 2):
    print(i, end=' ')
print()

print('----------')

print('<구구단>')
#내가 푼거
for i in range(2,10):
    print('<',i,'단>')
    for j in range(2, 10):
        print(i,'*', j,'=', i * j)

#샘 코드
for i in range(2, 10):
    print('<<'+str(i)+'단>>')
    for j in range(1,10):
        print(str(i)+' * '+str(j)+' = '+str(i*j))
        #print(i, '*', j, '=', i*j, sep=' ')
    print()