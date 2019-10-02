a=input("输入字符串1：")
b=input("输入字符串2：")
list1=list(a)
list2=list(b)
print("字符串1的长度：",len(a))
list1.reverse()
print("反序:" ,"".join(list1))
print("字符串1与2结合:",a+b)
set1=set(list1)
set2=set(list2)
if set1<=set2 :
    print("a是b的子集")
else:
    print("a不是b的子集")



