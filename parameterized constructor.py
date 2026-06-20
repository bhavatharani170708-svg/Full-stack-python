class student:
    def__init__(self, name):
        self.name=name 
        print("student name:",self.name)
    
 
    def__del__(self):
        print("student object destroyed")
S = student("ravi")
del S