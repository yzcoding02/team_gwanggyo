def 짝수(숫자):
    a=[]
    for i in range(2,숫자*2+1):
        if i%2==0:
            a.append(i)
    a.reverse()
    print(a)
짝수(3)
짝수(6)