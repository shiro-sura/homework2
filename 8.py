x=input("输入字符串：")
y=input("输入检索内容：")
list1=list(x)
if y in list1:
    z=list1.index(y)
    print("存在,位置在：" ,z+1)
else:
    print("不存在。")
