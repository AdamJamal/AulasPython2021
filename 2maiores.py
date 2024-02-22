def two_largest(inlist):
    if inlist[0] > inlist[1]:
        largest = inlist[0]
        second_largest = inlist[1]
    else: 
        largest = inlist[1] 
        second_largest = inlist[0] 
    
    for item in inlist[2:]:
        if item > largest:
            second_largest = largest
            largest = item
        elif largest > item > second_largest:
            second_largest = item
    
    return second_largest,largest

n1=(float(input()))
n2=(float(input()))
n3=(float(input()))
n4=(float(input()))
n5=(float(input()))

if __name__ == "__main__":
    inlist = [n1,n2,n3,n4,n5]
    print (two_largest(inlist))    