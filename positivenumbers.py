list1 = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    a = int(input("Enter a number: "))
    list1.append(a)
print([j for j in list1 if j>=0])

