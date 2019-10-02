x=int(input("第几项:"))
a=0
b=1
list1=list()
while b<20000:
    list1.append(b)
    a,b=b,a+b
print(list1[x-1])
