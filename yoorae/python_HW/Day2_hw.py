'''
조건문
->:Space/tab
1.If/Else
    if 조건:
        ->참일때 작성
    else:
        ->거짓일때 작성
2.For
    for i in range(숫자):
        ->작성
    for i in range(시작,끝):
        ->작성
    for i in range(시작,끝,증감):
        ->작성
'''
# 1~10까지의 수중에 홀수 출력
for i in range(1,11):
    if i%2==1:
        print(i)
# 1~10까지의 수중에 짝수 출력
for i in range(2,11):
    if i%2==0:
        print(i)
# 20~40까지의 수중에 3의 배수 출력
for i in range(20,41):
    if i%3==0:
        print(i)
# 20~40까지의 수중에 3과 4의 공배수 출력
for i in range(50,101):
    if i%3==0:
        if i%4==0:
            print(i)
# 1~100까지의 수중에 짝수들의 합과 홀수들의 합의 차 출력
sum=0
some=0
for i in range(1,101):
    if i%2==0:
        sum+=i
    if i%2==1:
        some+=i
print(sum-some)
# 1~20까지의 수중에 7의 배수 출력
sum=1
for i in range(1,21):
    if i%7==0:
        sum*=i
print(sum)