import turtle as t
t.speed(0)
t.color("skyblue","wheat")
t.pensize(10)
t.shape("turtle")

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def pal():
    t.circle(100)
    t.penup()
    t.left(90)
    t.backward(200)
    t.right(90)
    t.pendown()
    t.circle(100)
    

t.onscreenclick(move)
t.onkeypress(pal,"8")
    
t.listen()
t.mainloop()