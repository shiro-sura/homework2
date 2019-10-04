x=int(input("输入m值："))
y=int(input("输入n值："))
list2=list()
if x>0 and y>0 and x<y:
    for i in range(x,y+1):
        list1=list(str(i))
        list1.reverse()
        x="".join(list1)
        list2.append(x)
print(list2)
list3=list()
for b in list2:
    for c in range(2,int(b)):
        if int(b)%c==0:
            break
        else:
            list3.append(b)
list3=set(list3)
print(list3)

        
                
        
        

