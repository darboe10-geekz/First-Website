import turtle
import math 

# t = turtle.Turtle()
# t.speed(0)
# t.color('red')
# turtle.bgcolor('black')

# def corazon(n):
#     x = 16 * math.sin(n) ** 3
#     y = 13 * math.cos(n) - 5 * \
#         math.cos(2*n) - 2*math.cos(3*n) - \
#         math.cos(4*n)
#     return x, y

# t.penup ()
# for i in range(15):
#     t.goto(0, 0)
#     t.pendown()
#     for n in range(0, 100, 2):
#         x, y = corazon(n/10)
#         t.goto(x*i, y*i)
#     t.penup()

#     t.hideturtle()
#     turtle.done()


def xt(t):
    return 13*math.sin(t)**3
        
def yt(t):
    return 13*math.cos(t) -5*\
            math.cos(2*t)-2*\
            math.cos(3*t)-\
            math.cos(4*t)

t = turtle.Turtle()
t.speed(500)
turtle.bgcolor ('black')

for i in range (2550):
    t.goto((xt(i)*20, yt(i)*20))
    t.pencolor('red')
    t.goto(0, 0)
            