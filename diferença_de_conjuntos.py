n1,n2,n3,n4,n5,n6,n7,n8,n9,n10=int(input("valor:")).split()

A = {n1,n2,n3,n4,n5}
B = {n6,n7,n8,n9,n10}
z= A.symmetric_difference(B)

print(z)
