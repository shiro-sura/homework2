x=input("请输入字符串：")
list1=list(x)
zm=0
sz=0
qt=0
for i in list1:
    if 48<=ord(i)<=57 :
        sz+=1
    elif 65<=ord(i)<=90 or 97<=ord(i)<=122:
        zm+=1
    else:
        qt+=1
print("字母：",zm,"数字：",sz,"其他：",qt)
    
