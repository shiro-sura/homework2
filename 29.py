x=input("请输入体重：")
y=input("请输入身高：")
class BMI():
    def __init__(self,weight,height):
        self.weight=weight
        self.height=height

per1=BMI(x,y)
a=float(per1.weight)
b=float(per1.height)
print(a/(b**2))

      
    
