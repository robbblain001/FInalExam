# main trutle
import turtle

#dave = turtle.Turtle()
wn = turtle.Screen()
alex = turtle.Turtle()


def winders():
    alex.penup()
    alex.left(135)
    alex.forward(58)
    alex.left(90)
    alex.pendown()
    alex.forward(53)
    alex.right(90)
    alex.forward(55)
    alex.right(90)
    alex.forward(53)
    alex.right(90)
    alex.forward(55)
    alex.penup()
    alex.left(180)
    alex.forward(65)
    alex.left(90)
    alex.pendown()
    alex.forward(53)
    alex.right(90)
    alex.forward(65)
    alex.right(45)
    alex.forward(35)
    alex.right(45)
    alex.forward(30)
    alex.right(90)
    alex.forward(88.5)
    alex.penup()


def drawbed():
    alex.penup()
    alex.left(90)
    alex.forward(77.5)
    alex.left(90)
    alex.forward(212)
    alex.right(90)
    alex.forward(38)
    alex.pendown()
    alex.left(135)
    alex.forward(52)
    alex.left(180)
    alex.forward(53)
    alex.left(45)
    alex.forward(10)
    alex.left(135)
    alex.forward(68)


def drawwheel():
    alex.pendown()
    for i in range(240):
        alex.forward(1)
        alex.left(1.5)
    alex.penup()


def drawinwheel():
    for i in range(144):
        alex.forward(1)
        alex.left(2.5)


def bfender():
    alex.left(90)
    for i in range(180):
        alex.forward(0.75)
        alex.right(1)


def ffender():
    alex.left(90)
    for i in range(180):
        alex.forward(0.75)
        alex.right(1)


# start
alex.penup()
alex.setposition(-110, -195)
alex.speed(0)

# wheels
# outerwheels
# 1
alex.pendown()
drawwheel()
# 2
alex.setposition(100, -195)
drawwheel()

# innerwheels
# 1
alex.penup()
alex.setposition(-110, -180)
alex.pendown()
drawinwheel()
# 2
alex.penup()
alex.setposition(100, -180)
alex.pendown()
drawinwheel()

# rims
# 1
for i in range(18):
    alex.penup()
    alex.setposition(-110, -158)
    alex.pendown()
    alex.forward(22)
    alex.left(20)
# 2
for i in range(18):
    alex.penup()
    alex.setposition(100, -158)
    alex.pendown()
    alex.forward(22)
    alex.left(20)

# bottom
# back
alex.penup()
alex.setposition(-175, -135)
alex.pendown()
alex.forward(20)
bfender()
# front
alex.left(90)
alex.forward(125)
ffender()

# front
alex.left(90)
alex.forward(20)

for i in range(90):
    alex.forward(0.375)
    alex.left(0.5)
alex.left(45)
alex.forward(40)

for i in range(90):
    alex.forward(0.375)
    alex.left(0.5)

# hood/windsheild
alex.left(45)
alex.forward(65)
alex.right(45)
alex.forward(75)

# roof/bed
alex.left(45)
alex.forward(150)
alex.left(90)
alex.forward(60)
alex.right(90)
alex.forward(110)
alex.left(90)
alex.forward(77.5)
alex.left(90)
alex.forward(22)

# bedbars
alex.penup()
alex.forward(300)
alex.pendown()
drawbed()

# draw windows
winders()

'''
#colour
alex.pencolor("red")
alex.setposition(270,-120)
alex.pendown()
alex.forward(10)
'''



def lights():
    alex.setposition(48.5, 3)
    alex.pendown()
    alex.right(90)
    alex.forward(10)
    alex.right(90)
    alex.forward(15)
    alex.right(90)
    alex.forward(12)
    alex.penup()

lights()

def shocks():
    alex.pendown()
    alex.forward(4)
    alex.right(45)
    alex.forward(8)
    alex.left(90)
    alex.forward(8)
    alex.right(90)
    alex.forward(8)
    alex.left(90)
    alex.forward(8)
    alex.right(90)
    alex.forward(8)
    alex.penup()
    alex.forward(100)


def shocks2():
    alex.pendown()
    alex.forward(4)
    alex.right(45)
    alex.forward(7)
    alex.left(90)
    alex.forward(7)
    alex.right(90)
    alex.forward(7)
    alex.left(90)
    alex.forward(7)
    alex.right(90)
    alex.forward(7)
    alex.penup()
    alex.forward(100)


alex.setposition(90, -91)
shocks2()
alex.setposition(95, -91)
alex.left(45)
shocks2()
alex.setposition(103, -91)
alex.left(45)
shocks2()
alex.setposition(108, -91)
alex.left(45)
shocks2()

#putting the shocks in the right place
alex.setposition(-99, -91.5)
alex.left(45)
shocks2()
alex.setposition(-104, -91.5)
alex.left(45)
shocks2()
alex.setposition(-113, -91.5)
alex.left(45)
shocks2()
alex.setposition(-118, -91.5)
alex.left(45)
shocks2()

# drawing mirrors on the side of the truck
def mirrors():
    alex.setposition(103, -45)
    alex.left(135)
    alex.left(180)
    alex.pendown()
    alex.forward(15)
    alex.penup()
    alex.setposition(103, -53)
    alex.pendown()
    alex.right(90)
    alex.forward(8)
    alex.left(180)
    alex.forward(5)









# call on mirrors

mirrors()






# end of program that calls the turtle to stop


'''
# end
alex.penup()
alex.forward(500)
'''
turtle.done()















