i = 1
while i <= 10:
    if i > 5:
        break # break로 종료되는 것은 정상종료 아님 / 중간에 멈춘걸로 됨
    print(i)
    i += 1
else:
    print('i', i, sep='=')
    
for i in range(1, 10):
    if i % 2 == 0:
        continue #마지막까지 for문은 계속 돌고나서 끝남
    print(i)
else:
    print('i', i, sep='=')