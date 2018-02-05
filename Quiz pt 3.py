import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

def draw_line(t,Length,Color,line_type):
    """which uses turtle, t, to draw a line of
length, Length, and of color, Color & where
line_type describes what the turtle will draw """
    if line_type == 1:
        for i in range(5):
            tess.fd(Length/5)
    elif line_type == 2:
        pen_down = 1
        for i in range(9):
            seg_length = Length/9
            if pen_down == 1:
                tess.pd()
                pen_down = 0
            else:
                tess.pu()
                pen_down= 1
            tess.fd(seg_length)
    elif line_type == 3:
        pen_down = 1
        for i in range(9):
            seg_length = Length/9
            if pen_down == 1:
                tess.pd()
                pen_down = 0
            else:
                tess.pu()
                # go have seg_length
                # dot
                # go have seg_length
                pen_down= 1
            tess.fd(seg_length)

t,Length,Color= tess, 200 , 'red'
for i in range(1,4):
    draw_line(t,Length,Color,i)
    t.lt(90) 
            
            
