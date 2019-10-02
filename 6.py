import random
list1=list()
x=1
while x<=4:
    y=random.randint(0,9)
    list1.append(y)
    x+=1
z="".join('%s' %id for id in list1)
print("验证码为：",z)
f=1
while f==1:
    y=input("请输入验证码：")
    if z==y:
        print("验证成功！")
        break
    else:
        print("验证失败")
  
