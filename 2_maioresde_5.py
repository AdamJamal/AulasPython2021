n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())

integers = [n1,n2,n3,n4,n5]

copy_of_integers = integers[:]  

largest_integer = max(copy_of_integers) 
copy_of_integers.remove(largest_integer)

second_largest_integer = max(copy_of_integers) 

print(largest_integer, second_largest_integer)