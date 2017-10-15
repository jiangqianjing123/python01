import turtle as t
import time  
import os  
#  
def  draw_square(org_x, org_y, x, y):  
    t.setpos(org_x, org_y)  # to left and bottom connor  
    t.color('red', 'red')  
    t.begin_fill()  
    t.fd(x)  
    t.lt(90)  
    t.fd(y)  
    t.lt(90)  
    t.fd(x)  
    #print(turtle.pos())  
    t.lt(90)  
    t.fd(y)  
    t.end_fill()  
  
def draw_star(center_x, center_y, radius):  
    print(center_x, center_y)  
    t.pencolor('black')  
    t.setpos(center_x, center_y)  
    pt1 = t.pos()  
    t.circle(-radius, 360 / 5)  
    pt2 = t.pos()  
    t.circle(-radius, 360 / 5)  
    pt3 = t.pos()  
    t.circle(-radius, 360 / 5)  
    pt4 = t.pos()  
    t.circle(-radius, 360 / 5)  
    pt5 = t.pos()  
    t.color('yellow', 'yellow')  
    t.begin_fill()  
    t.goto(pt3)  
    t.goto(pt1)  
    t.goto(pt4)  
    t.goto(pt2)  
    t.goto(pt5)  
    t.end_fill()  
print(t.pos())  
  
t.pu()  
draw_square(-320, -260, 660, 440)  
star_part_x = -320  
star_part_y = -260 + 440  
star_part_s = 660 / 30  
center_x, center_y = star_part_x + star_part_s * 5, star_part_y - star_part_s * 5  
t.setpos(center_x, center_y)  # big star center  
t.lt(90)  
draw_star(star_part_x + star_part_s * 5, star_part_y - star_part_s * 2, star_part_s * 3)  
  
# draw 1st small star  
t.goto(star_part_x + star_part_s * 10, star_part_y - star_part_s * 2)    # go to 1st small star center  
t.lt(round(t.towards(center_x, center_y)) - t.heading())  
t.fd(star_part_s)  
t.rt(90)  
draw_star(t.xcor(), t.ycor(), star_part_s)  
  
# draw 2nd small star  
t.goto(star_part_x + star_part_s * 12, star_part_y - star_part_s * 4)    # go to 1st small star center  
t.lt(round(t.towards(center_x, center_y)) - t.heading())  
t.fd(star_part_s)  
t.rt(90)  
draw_star(t.xcor(), t.ycor(), star_part_s)  
  
# draw 3rd small star  
t.goto(star_part_x + star_part_s * 12, star_part_y - star_part_s * 7)    # go to 1st small star center  
t.lt(round(t.towards(center_x, center_y)) - t.heading())  
t.fd(star_part_s)  
t.rt(90)  
draw_star(t.xcor(), t.ycor(), star_part_s)  
  
# draw 4th small star  
t.goto(star_part_x + star_part_s * 10, star_part_y - star_part_s * 9)    # go to 1st small star center  
t.lt(round(t.towards(center_x, center_y)) - t.heading())  
t.fd(star_part_s)  
t.rt(90)  
draw_star(t.xcor(), t.ycor(), star_part_s)  
t.ht()  
time.sleep(5)  



