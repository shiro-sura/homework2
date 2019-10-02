x=int(input(" 请输入年份："))
c1=x%4==0 and x%100!=0
c2=x%4==0 and x%400==0
if x==c1 or c2:
    print("闰年")
else:
    print("不是闰年")
