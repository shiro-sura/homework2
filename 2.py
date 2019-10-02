x=int( input("请输入正整数："))
y=1
z=0
if x < 0:
    print("没有阶乘，请输入正整数")
elif x==0:
    print("请输入正整数")
else:
    for i in range(1,x+1):
        y=i*y
        z=z+y
    print(z)
