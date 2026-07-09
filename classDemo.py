# class= data method + method

# putting data and functions into one unit is called encapsulation 

class Student:
    college_name="BIET"
    def assign(self,name,usn,marks):
        self.name=name        #self.name is instance variable
        self.usn=usn
        self.marks=marks
    
    def display(self):
        print(f"name : {self.name}\nusn : {self.usn}\nMarks : {self.marks}")



s1=Student()               #s1=object of the class student 

# print(s1,type(s1))
if __name__=="__main__":
    s1.assign("karthik","cv040",[69,55,80])


    print(f"Student s1 is")
    s1.display()
    print(f"College name is : {s1.college_name}")
    #above line fetching class variable using object name

    print(f"College Name is : {Student.college_name}")
    #above line fetching class varianble using class name

