n=1
while n==1:
    x=input("请输入18位身份证号：")
    y=len(x)
    if y==18:
        list1=list(x)
        year="".join(list1[6:10])
        month="".join(list1[10:12])
        day="".join(list1[12:14])
        sex=list1[16]
        if int(sex)%2==0:
            print(year,"年",month,"月",day,"日","性别：男")
        else:
            print(year,"年",month,"月",day,"日","性别：女")
        break
    else:
        print("请重新输入。")

      
