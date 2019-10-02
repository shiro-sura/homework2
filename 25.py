import random
pd=1
print("欢迎来到猜数字游戏。")
x=random.randint(0,101)
while pd<=7:
    y=int(input("请输入你的数字："))
    if x==y:
        print("恭喜你猜对啦")
        break
    else:
        print("猜错啦")
        if y<x:
            print("输入的数太小啦")
        else:
            print("输入的数过大啦")
        z=7-pd
        print("你还有",z,"次机会")
        pd+=1
print("游戏结束")
