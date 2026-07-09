class Data:

    def __init__(self,x,y):
        self.x=x
        self.y=y


class Sum(Data):

    def __init__(self, x, y):
        super().__init__(x, y)

    def calculate(self):
        print(f"Sum = {self.x+self.y}")


class Sub(Data):

    def __init__(self, x, y):
        super().__init__(x, y)

    def calculate(self):
        print(f"Sub = {self.x-self.y}")



if __name__=='__main__':
    d1=Data(20,10)

    d1=Sum(20,10)
    d1.calculate()

    d1=Sub(20,10)
    d1.calculate()
