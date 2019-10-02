import random
x=int(input("想要多少数："))
y=int(input("想要第几大："))
list1=list()
list2=list()
for i in range(1,x+1):
    list1.append(i)
    list2.append(i)
random.shuffle(list1)
print(list1)
list2.sort(reverse=True)
print(list2)
print(list2[y-1])

