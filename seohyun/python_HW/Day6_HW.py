def 짝수(a):
    list=[]
    for i in range(a*2):
        if i%2==0:
            list.append(i)
            list.sort()
            list.reverse()
    print(list)
짝수(9)