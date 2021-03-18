import numpy as np
import math
from operator import add

print("Enter point coordinates: ")
a=int(input())
b=int(input())
c=int(input())
p = [a,b,c] #point

axes = ['x','y','z']
print(p)
for i in axes:
    new_p = []  #new points
    print("Rotation w.r.t " + i + "-axis(in degrees,in anti-clock wise direction):")
    degrees = math.radians(int(input()))
    if i=='x':
        new_p.append(p[0])
        new_p.append((p[1]*math.cos(degrees)) - p[2]*math.sin(degrees))
        new_p.append((p[1]*math.sin(degrees)) + p[2]*math.cos(degrees))
    if i=='y':
        new_p.append((p[0]*math.cos(degrees)) - p[2]*math.sin(degrees))
        new_p.append(p[1])
        new_p.append((p[0]*math.sin(degrees)) + p[2]*math.cos(degrees))
    if i=='z':
        new_p.append((p[0]*math.cos(degrees)) - p[1]*math.sin(degrees))
        new_p.append((p[0]*math.sin(degrees)) + p[1]*math.cos(degrees))
        new_p.append(p[2])

    p = new_p

print("point coordinates after rotations = ")
print(p)

print("Enter the translations w.r.t x,y,z respectively: ")
trans = [int(input()) for i in range(3)]
p_t = list(map(add, p, trans)) #point after translations.
print(p_t)
