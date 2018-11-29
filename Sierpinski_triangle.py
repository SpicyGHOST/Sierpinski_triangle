#!usr/bin/python
# -*- coding:utf-8 -*-
import random as ran
import turtle as t
import math

"""
k stands for one unit,for 1920*1080 resolution,
600 is better,if your screen is not big enough,
please reduce it

k代表一个单位长度,对于1920*1080分辨率的屏幕,
k取600较好,如果你的屏幕太小,请减小k的值
"""
k=int(input("Please enter one unit:"))

Ax=-k/2
Ay=-k/2/math.sqrt(3)
Bx=k/2
By=-k/2/math.sqrt(3)
Cx=0
Cy=k/math.sqrt(3)
x=ran.randint(int(Ax)+1,int(Bx))
y=ran.randint(int(Ay)+1,int(Cy))

t.pensize(1)
t.speed(9999)
t.pencolor("black")
a={"0":"red","1":"green","2":"blue"}

def draw(x,y):
    t.pencolor(a[str(i%3)])
    t.up()
    t.goto(x,y)
    t.down()
    t.forward(1)

#It's a dead loop and can run forever
#这是个死循环，可以永远运行下去
for i in range(99999):
    if ran.randint(1,3)==1:
        x=(x+Ax)/2
        y=(y+Ay)/2
        draw(x,y)
    if ran.randint(1,3)==2:
        x=(x+Bx)/2
        y=(y+By)/2
        draw(x,y)
    if ran.randint(1,3)==3:
        x=(x+Cx)/2
        y=(y+Cy)/2
        draw(x,y)
