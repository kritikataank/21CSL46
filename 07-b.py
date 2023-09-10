class Employee:
    def __init__(self):
        self.name =""
        self.empID = ""
        self.dept = ""
        self.salary = 0


    def getempdetails(self):
        self.name = input("Enter Employee name: ")
        self.empID = input("Enter Employee ID: ")
        self.dept = input("Enter Employee Department: ")
        self.salary = int(input("Enter Employee Salary: "))


    def showempdetails(self):
        print("Employee Details")
        print("Name : ", self.name)
        print("Employee ID : ", self.empID)
        print("Department : ", self.dept)
        print("Salary : ", self.salary)

    def updtsalary(self):
        self.salary = int(input("Enter new salary: "))
        print("Updated Salary: ", self.salary)

e1=Employee()
e1.getempdetails()
e1.showempdetails()
e1.updtsalary()