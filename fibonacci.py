first,second = 0,1
print("FIBONACCI SERIES")
n = int(input("Enter a positive integer: "))
if n==1:
    print(first,end=" ")
elif n==2:
    print(first,second ,end=" ")
else:
    print(first,second,end=" ")
    
    for i in range(2,n):
        c = first + second
        print(c,end = " ")
        first = second
        second = c
        
        
    
    
