'''
1/ 1~10 홀수 출력
for i in range(1,11,2):
  if i%2==1:
   print(i)

2/ 1~10 짝수 출력
for i in range(2,11,2):
  if i%2==0:
   print(i)

3/ 20~40 3의 배수 출력
for i in range(20,41):
  if i%3==0:
    print(i)

4/ 50~100 3과4의 공배수 출력
for i in range(50,101):
  if i%3==0:
    if i%4==0:
print(i)

5/ 1~100 짝수들의 합과 홀수들의 합의 차
sum=0
minus=0
for i in range(1,101):
  if i%2==0:
    sum+=i
  if i%2==1:
    minus+=i
print(sum-minus)

6/ 1~20 7의 배수들의 곱
sum=1
for i in range(1,21):
  if i%7==0:
    sum*=i
print(sum)
'''
