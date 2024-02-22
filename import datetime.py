import datetime
d1=int(input())
m1=int(input())
y1=int(input())
d2=int(input())
m2=int(input())
y2=int(input())

from datetime import date
d0 = date(y1,m1,d1)
d1 = date(y2,m2,d2)
delta = d1 - d0
from math import floor
if d1>d0:
    print("0")
if d0>d1:    
    print(floor(delta.days/365))