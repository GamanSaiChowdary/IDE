class Parent:
    def __init__(self,text):
        self.message=text
    def printMessage(self):
        print(self.message)
class Child(Parent):
    def __init__(self,text):
        super().__init__(text)
a=Child("Hello this is Python Class")
a.printMessage()
