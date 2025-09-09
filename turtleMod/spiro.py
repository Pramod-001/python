import turtle as t
import random
trtl = t.Turtle()
trtl.shape("turtle")
t.colormode(255)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
col = (r,g,b)
trtl.speed("fastest")
#Circle
for i in range(100) :
    trtl.color(col)
    trtl.circle(100)
    trtl.left(5)
print(trtl.position())
