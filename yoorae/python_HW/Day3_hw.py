# 1
for i in range(1,11):
        print(i)

i=1
while i<11:
    print(i)
    i+=1
# 2
for i in range(1,11):
    if i%2==0:
        print(i)

i=1
while i<11:
    if i%2==0:
        print(i)
    i+=1
# 3
sum=0
for i in range(1,11):
    if i%3==0:
        sum+=i
print(sum)

sum=0
i=1
while i<11:
    if i%3==0:
        sum+=i
    i+=1    
print(sum)
# 4
for i in range(50,101):
    if i%3==0:
        if i%7==0:
            print(i)

i=50
while i<101:
    if i%3==0:
        if i%7==0:
            print(i)
    i+=1
# 5
sum=1
for i in range(1,21):
    if i%2==0:
        sum*=i
print(sum)

sum=1
i=1
while i<21:
    if i%2==0:
        sum*=i
    i+=1    
print(sum)