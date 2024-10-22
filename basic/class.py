class Student:
    def __init__(self,name):
        self.name = name
        
    def getName(self):
        return self.name    
    
    
std = Student("Sourav")

print(f"My name is {std.getName()}")