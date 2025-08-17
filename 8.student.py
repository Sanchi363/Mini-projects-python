class student:
    no=0
    def __init__(self):
       self.subject=[]
    def addnew(self,name,r,subject,g):
        for i in subject:
            self.subject.append(i)
        self.name=name
        self.roll=r
        self.grade=g
        student.no=student.no+1
    def display(self):
        print(f"Name:{self.name}")
        print(f"Roll number:{self.roll}")
        print("Subjects:")
        for i in self.subject:
            print(f"{i}")
        print(f"Grade:{self.grade}")
    def number():
        print(f"Total number of students:{student.no}")
    def update(self,g):
        self.grade=g
        print(f"Grade Updated to {self.grade}")
a=student()
n="Sanchi"
roll="157"
subject=["OOPS","OS","TAFL"]
a.addnew(n,roll,subject,"B")
a.display()
b=student()
b.addnew("Y","217",["CS","DS","TC"],"A")
b.display()
student.number()
a.update("A")
a.display()