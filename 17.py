x=int(input("输入数字："))
list1=list()
for i in range(1,x+1):
    list1.append(i)
print(list1)
list2=list()
y=len(list1)
n=0
while n<=y-1:
    list1_copy=list1.copy()
    list1_copy.pop(n)
    a=1
    for z in list1_copy:
        a*=z
    n+=1
    list2.append(a)
print(list2)
    

