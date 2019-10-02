x=int(input("输入数字："))
list1=list()
for i in range(1,x+1):
    if i%3==0 or i%5==0:
        list1.append(i)
print(list1)
a=0        
for z in list1:
    a+=z
print(a)
    
