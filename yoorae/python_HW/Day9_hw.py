# 1-1
a=[]
for i in range(1,101):
    if i%3==0:
        if i%4==0:
            a.append(i)
print(a)
# 1-2
print(a[4:])
# 1-3
print(a[:3])
# 1-4
print(a[3:5])