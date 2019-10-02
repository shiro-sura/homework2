x=input("请输入字符串：")
list1=list(x)
y=list1[:-9:-1]
list2=list(y)
list2.reverse()
z="".join(list2)
x="back-end"
if x==z:
    print("yes")
else:
    print("no")

