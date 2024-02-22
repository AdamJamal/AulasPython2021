n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

list1 = [n1,n2,n3,n4,n5]
 
list2 = list(set(list1))
 
list2.sort()
 
print(list2[-2], list2[-1])