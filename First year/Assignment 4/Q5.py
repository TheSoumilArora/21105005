class Employee:                                                                                         #Creating class Employee
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print("%s has a salary of %d rupees" % (name,salary))
    def __delete__(self,name):
        if hasattr(Employee,'self.name') == name:
            print(123)
        print("All deleted, i.e. %s" % (self.name))

print("The data is stored where:")
employee1 = Employee("Mehak",40000)
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)

'''
print("\na. Updated the salary of %s from %d to " % (employee1.name,employee1.salary), end = "")
employee1.salary = 70000
print(employee1.salary)
'''
employee3.__delete__("Viren")
print("")

