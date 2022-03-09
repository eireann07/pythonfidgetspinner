#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:57:20 2022

@author: Erin
"""
from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'violet')
    back (100)
    right (120)
    forward(100)
    dot(120, 'teal')
    back (100)
    right(120)
    forward(100)
    dot(120, 'DarkOrchid4')
    back(100)
    right(120)
    update()
def animate ():
    if state ['turn']>0:
        state ['turn'] -=1
    
    spinner()
    ontimer(animate, 20)
def flick ():
    state['turn'] +=10
        
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()