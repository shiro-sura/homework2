x=int(input("请输入一个正整数："))
if x<=0:
    print("输入错误。")
else:
    list1=list(str(x))
    list1.reverse()
while list1[0]=="0":
    del list1[0]
print("".join(list1))
    
