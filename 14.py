x=int(input("请输入第一个数："))
y=int(input("请输入第二个数："))
z=int(input("请输入第三个数："))
if x>y:
    if x>z:
        print('x是最大值:',x)
    else:
        print('z是最大值:',z)
elif x>z:
    if x>y:
        print('x是最大值:',x)
    else:
        print('y是最大值：',y)
else:     
    if y>z:
        print('y是最大值：',y)
    else:
        print('z是最大值：',z)
