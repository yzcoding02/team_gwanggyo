리스트=[]
for i in range(1,100):
    if i%3==0:
        if i%4==0:
            리스트.append(i)
print(리스트)
print(리스트[4:])
print(리스트[:3])
print(리스트[2:5])