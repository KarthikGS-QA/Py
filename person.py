class Person:
    def assign(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(f"Name :{self.name}\nAge : {self.age}")

    def findElder(self,p2):
        if self.age>p2.age:
            return self
        else:
            return p2




if __name__=="__main__":
    p1=Person()

    p1.assign("Karthik",28)

    print("person details of person p1")
    p1.display()


    p2=Person()

    p2.assign("Tirtu",24)
    print("person details of person p2")
    p2.display()

    # elder= p1 if p1.age>p2.age else p2

    # # print(f"{elder}")
    # print("Elder person between p1 and p2 is   ")
    # elder.display()
    elder=Person()

    elder=p1.findElder(p2)
    print(f"-------------------elder Person--------------")
    elder.display()



