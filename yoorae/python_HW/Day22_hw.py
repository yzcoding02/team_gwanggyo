import turtle as t
t.shape("turtle")
t.color("skyblue","wheat")
t.speed(1)
t.pensize(5)

def sagakhyung(x,y,length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.penup()
    t.home()
    t.pendown()
sagakhyung(-700,200,200)
sagakhyung(400,80,50)
sagakhyung(-400,-100,20)
sagakhyung(350,-200,150)
t.clear()

def ogakhyung(x,y,length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(5):
        t.forward(length)
        t.right(72)
    t.penup()
    t.home()
    t.pendown()
ogakhyung(-700,200,200)
ogakhyung(400,80,50)
ogakhyung(-400,-100,20)
ogakhyung(350,-150,150)
t.clear()

def sipgakhyung(x,y,length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(10):
        t.forward(length)
        t.right(36)
    t.penup()
    t.home()
    t.pendown()
sipgakhyung(-600,250,100)
sipgakhyung(400,80,20)
sipgakhyung(-400,-100,15)
sipgakhyung(350,-150,70)
t.clear()

def sipgakhyung(x,y,length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(360):
        t.forward(length)
        t.right(1)
    t.penup()
    t.home()
    t.pendown()
sipgakhyung(-600,250,2)
sipgakhyung(400,80,1)
sipgakhyung(-400,-100,0.5)
sipgakhyung(350,-150,1.5)
t.clear()
t.mainloop()