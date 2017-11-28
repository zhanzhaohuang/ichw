"""planets.py: Description of what planets does.

__author__ = ""zhanzhaohuang
__pkuid__  = "1700011730"
__email__  = "1700011730@pku.edu.cn"
"""
import turtle

def rb(i):
    """description of rb, using i, return the distance that b moves
    """
    if i < 90:
        i=i/100+1
    else:
        i=1.9-(i-90)/100
    return i
def rc(i):
    """description of rc, using i, return the distance that c moves
    """
    if i < 90:
        i=i/80+3
    else:
        i=4.125-(i-90)/80
    return i
def rd(i):
    """description of rd, using i, return the distance that d moves
    """
    if i < 90:
        i=i/50+4
    else:
        i=6.8-(i-90)/50
    return i
def re(i):
    """description of re, using i, return the distance that e moves
    """
    if i < 90:
        i=i/40+5
    else:
        i=7.25-(i-90)/40
    return i
def rf(i):
    """description of rf, using i, return the distance that f moves
    """
    if i < 90:
        i=i/30+6
    else:
        i=9-(i-90)/30
    return i


def main(wn,aa,b,c,d,e,f,g,n):
    """main module
    """
    wn=turtle.Screen()
    aa=turtle.Turtle()
    b=turtle.Turtle()
    c=turtle.Turtle()
    d=turtle.Turtle()
    e=turtle.Turtle()
    f=turtle.Turtle()
    g=turtle.Turtle()

    for i in [aa,b,c,d,e,f,g]:
        i.shape("circle")
    
    aa.color("blue")
    b.color("green")
    c.color("red")
    d.color("black")
    e.color("cyan")
    f.color("orange")
    g.color("yellow")

    aa.pencolor("blue")
    b.pencolor("green")
    c.pencolor("red")
    d.pencolor("black")
    e.pencolor("cyan")
    f.pencolor("orange")
    g.pencolor("yellow")

    n=50
    for i in [aa,b,c,d,e,f]:
        i.up()
        i.forward(n)
        i.down()
        i.left(90)
        n=n*3/2
    for p in range(10086):
        for i in range(180):
            aa.forward(0.75)
            aa.left(1)
    
            b.forward(rb(i))
            b.left(1)
    
            c.forward(rc(i))
            c.left(1)
    
            d.forward(rd(i))
            d.left(1)
        
            e.forward(re(i))
            e.left(1)
        
            f.forward(rf(i))
            f.left(1)

if __name__ == '__main__':
    main(wn,aa,b,c,d,e,f,g,n)
