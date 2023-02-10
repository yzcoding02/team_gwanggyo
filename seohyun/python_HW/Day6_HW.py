def 짝수(a):
    list=[]
    for i in range(2,a*2+1):
        if i%2==0:
            list.append(i)
            list.sort()
            list.reverse()
    print(list)
짝수(3)
짝수(6)