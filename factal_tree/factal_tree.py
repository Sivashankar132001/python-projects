import turtle

tu = turtle.Turtle()
tu1 = turtle.Turtle()
tu.screen.bgcolor("black")
tu1.screen.bgcolor("blue")
tu.pensize(2)
tu1.pensize(2)
tu.color("green")
tu1.color("yellow")

tu.left(90)
tu1.left(90)
tu.backward(100)
tu1.backward(100)
tu.speed(2000)
tu.shape('turtle')


def tree(i):
    if i<10:
        return
    else:
        tu.forward(i)
        tu.color("green")

        tu.circle(2)
        tu.color("blue")

        tu.left(30)
        tree(3*i/4)
        tu.right(60)
        tree(3*i/4)
        tu.left(30) 
        tu.backward(i)





tree(100)
turtle.done() 

