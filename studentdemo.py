class Student:

    # def assign(self,name,usn,marks):
    #     self.name=name
    #     self.usn=usn
    #     self.marks=marks

    object_count=0
    def __init__(self,name,usn,marks):               #Constructor declaration
        self.name=name
        self.usn=usn
        self.marks=marks
        Student.object_count+=1

    
    def display(self):

        print(f"Name  : {self.name}")
        print(f"USN   : {self.usn}")
        print(f"Marks : {self.marks}")
        print(f"No of object : {Student.object_count}")


    @classmethod
    def display_count(cls):
        print(f"No of object created = {cls.object_count}")

    
    @staticmethod
    def findSum(a,b):
        print(f"{Student.object_count}")
        return a+b



s1=Student("Raj","BE001",[40,50,66])         # constructor gets called

print("Student s1 is ...")
s1.display()


s2=Student("Kiran","BE002",[80,58,78])

print("Student s2 is ...")
s2.display()


s3=Student("Anu","BE003",[89,87,79])

print("Student s3 is ...")
s3.display()

print("No of object created are ....")
Student.display_count()                #Class method being called

print(f"")




# s1.assign("Raj","BE001",[40,50,66])
# s2.assign("Kiran","BE002",[80,58,78])
# s3.assign("Anu","BE003",[89,87,79])








