def 짝수(숫자):
    결과=[]
    for i in range(2,숫자*2+1):
        if i %2==0:
            결과.append(i)
    결과.reverse()
    print(결과)
짝수(3)
짝수(6)