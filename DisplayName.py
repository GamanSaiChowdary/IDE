class Student:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    def display(self):
        # print("First Name:",self.firstName)
        # print("Last:",self.lastName)
        print(self.firstName,self.lastName)

s1 = input("Enter your first name\n")
s2 = input("Enter your last name\n")
a = Student(s1, s2)
a.display()