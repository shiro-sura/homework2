x=input("请输入字符串：")
list1=list(x)
list2=list()
y=len(x)
n=0
while n<=y-1:
    q=list1[n]
    z=ord(q)
    list2.append(z)
    n+=1
print(list2)
