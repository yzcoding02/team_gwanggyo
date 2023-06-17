i=int(input("양의 정수를 넣어주세여><:"))
b=0
while i>0:
    i=i//10
    b+=1
print(f"이 수의 자리수는 {b}임미다><")