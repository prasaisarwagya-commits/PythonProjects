# Question 2: Employee Management System

# Create a Python class named "Employee".

# Requirements:

# - Define attributes such as employee ID, name, department, and salary.
# - Use a constructor ("init") to initialize employee details.
# - Create methods to display employee information and calculate annual salary.
# - Create at least three employee objects and display their details.



class Employee:
    def __init__(self, id , name , department , salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary


    def get_info(self):
        print(f'Employee id: {self.id}')
        print(f'Name: {self.name}')
        print(f'Department: {self.department}')
        print(f'Salary: {self.salary}')


    def annual_salary(self):
        annual_salary = self.salary * 12
        return annual_salary 
    

employee1 = Employee(1 , 'Kane' , 'Finance' , 50000)
employee2 = Employee(2, 'Dristy', 'Engineering', 65000)
employee3 = Employee(3, 'Lionel', 'Human Resources', 55000)





print('\n-------------------------------- ')
employee1.get_info()
print(f'Annual Salary: Rs {employee1.annual_salary()}')
print('\n-------------------------------- ')

print('\n-------------------------------- ')
employee2.get_info()
print(f'Annual Salary: Rs {employee2.annual_salary()}')
print('\n-------------------------------- ')


print('\n-------------------------------- ')
employee3.get_info()
print(f'Annual Salary: Rs {employee3.annual_salary()}')
print('\n-------------------------------- ')




