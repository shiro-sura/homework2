x=str(input("请输入字符串："))
y=len(x)
n=0
list1=list(x)
list2=list()
while n<=y-1:
    z=list1[n]
    if 65<=ord(z)<=90 :
        z=chr(ord(z)+32)
        list2.append(z)
        n+=1
    elif 97<=ord(z)<=122:
        z=chr(ord(z)-32)
        list2.append(z)
        n+=1
    else:
        z=z
        list2.append(z)
        n+=1
print("".join(list2))

