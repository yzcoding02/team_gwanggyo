import matplotlib.pyplot as plt
plt.figure()

x1=[]
x2=[]
x3=[]
x4=[]
y1=[]
y2=[]
y3=[]
y4=[]
for i in range(-5,6):
    x1.append(i)
    x2.append(i)
    x3.append(i)
    x4.append(i)

    y1.append(i+1)
    y2.append(i)
    y3.append(i)
    y4.append(-i-1)
plt.plot(x1,y1,x2,y2,x3,y3,x4,y4)
plt.show()