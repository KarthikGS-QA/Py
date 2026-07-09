class Complex():
    def __init__(self,a=None,b=None):
        self.a=a
        self.b=b

    # def findSum(self,obj):
    #     res=Complex(self,obj)
    #     res.a=self.a+obj.a
    #     res.b=self.b+obj.b
    #     return res

    def display(self):
        print(f"{self.a}+i{self.b}")
    

    def __add__(self, obj):      #  this is method overloading this is how it is done in py only we should use magic method to overload
        res=Complex(self,obj)
        res.a=self.a+obj.a
        res.b=self.b+obj.b
        return res


c1=Complex(3,4)
c2=Complex(5,10)


c3=Complex()

# c3=c1.findSum(c2)

c3=c1+c2 # c1.__add__(c2)        method overloading

c1.display()
c2.display()




print(f"c1+c2 =  ")

c3.display()