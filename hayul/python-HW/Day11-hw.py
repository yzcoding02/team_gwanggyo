import matplotlib.pyplot as plt
plt.figure()
xl=[]
yl=[]
x2=[]
y2=[]
x3=[]
y3=[]
for i in range(-10,11):
    xl.append(i)
    yl.append(i)
    x2.append(i)
    y2.append(i**2)
    x3.append(i)
    y3.append(i**3)
plt.plot(xl,yl,'b',x2,y2,'b',x3,y3,'b')
plt.show()