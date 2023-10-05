class Student:
    def get_data(self):
        self.rollno = int(input("enter the roll no:"))        
        self.student_name = input("enter the student name:")        
    def print_data(self):
        print("rollno =",self.rollno)
        print("student_name =",self.student_name)
class Marks(Student):
    
    def input_data(self):
        Student.get_data(self)
        self.physics = int(input("enter the marks:"))
        self.maths = int(input("enter the marks:"))
        self.english = int(input("enter the marks:"))
        self.chemistry = int(input("enter the marks:"))
        self.biology = int(input("enter the marks:"))
        self.malayalam = int(input("enter the marks:"))
    def out_data(self):
        self.total=(self.physics+self.maths+self.english+self.chemistry+self.biology+self.malayalam)
        print("result of roll no",self.rollno,"name", self.student_name,"is: for physics=",self.physics,"for maths = ",self.maths," for english = ",self.english," for chemistry = ",self.chemistry," for biology = ",self.biology," for malayalam = ",self.malayalam, "and total mark is: ",self.total)
        
obj1=Marks()
# obj1.get_data()
# obj1.print_data()
obj1.input_data()
obj1.out_data()
# obj1.sum()