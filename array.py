class Array:

    def __init__(self,a=None):
        self.a=a

    
    def __mul__(self, obj):
        temp=[]
        for i in range(0,len(self.a)):
            
            temp.append(self.a[i]*obj.a[i])
        res = Array(temp)
        return res
    def __truediv__(self, obj):
        temp=[]
        for i in range(0,len(self.a)):
            
            temp.append(self.a[i]/obj.a[i])
        res = Array(temp)
        return res
        

    def __add__(self, obj):
        temp=[]
        for i in range(0,len(self.a)):
            
            temp.append(self.a[i]+obj.a[i])
        res = Array(temp)
        return res
    
    def __sub__(self, obj):
        temp=[]
        for i in range(0,len(self.a)):
            
            temp.append(self.a[i]-obj.a[i])
        
        res=Array(temp)
        return res
    
    def display(self):

        print(f" {self.a}")



a1=Array([1,2,3,4])
a2=Array([4,5,6,7])


a3=Array()

a4=Array()

a5=Array()

a6=Array()

a3=a1+a2

a4=a2-a1

a5=a1*a2

a6=a2/a1


print(f"Array a1 is :")

a1.display()

print(f"Array a2 is :")
a2.display()


print(f"a1 + a2 is  :")
a3.display()

print(f"a2 - a1 is  :")
a4.display()


print(f"a1 * a2 is  :")
a5.display()

print(f"a2 / a1 is  :")
a6.display()


