from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days
     

d = int(input())
m = int(input())
a = int(input())

date1 = date(a, 1, 1)
date2 = date(a, m, d)
print(numOfDays(date1, date2))

