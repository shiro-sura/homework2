list1=list()
for i in range(100,999):
    list3=list(str(i))
    a=list3[0]
    b=list3[1]
    c=list3[2]
    if int(a)**3+int(b)**3+int(c)**3==i:
        list1.append(i)
print(list1)
    
