import turtle as t
t.speed(0)
t.color("skyblue","wheat")
t.pensize(10)
t.shape("turtle")

def samgakhyung(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(3):
        t.forward(100)
        t.left(120)
def sagakhyung(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)
def ogakhyung(x,y,):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(5):
        t.forward(100)
        t.right(72)
def allclear(x,y):
    t.clear()
    
t.onscreenclick(samgakhyung)
t.onscreenclick(sagakhyung,2)
t.onscreenclick(ogakhyung,3)
t.onclick(allclear)

t.mainloop()