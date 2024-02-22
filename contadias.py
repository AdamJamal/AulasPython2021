from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days
     

d = int(input())
m = int(input())
a = int(input())
if date==(2012,12,31):
    numOfDays==366
else:    
    date1 = date(a, 1, 1)
    date2 = date(a, m, d+1)
    print(numOfDays(date1, date2))