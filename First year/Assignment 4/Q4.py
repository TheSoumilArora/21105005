class Student:
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
    def __del__(self):
        print("Object destroyed")


        