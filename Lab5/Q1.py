class employee:
    Id = 0
    name = ""
    sal = 0.0
    dept = ""
    def __init__(self, Id, name, sal, dept):
        self.Id = Id
        self.name = name
        self.sal = sal
        self.dept = dept

    def create_tuple(self):
        return (self.Id, self.name, self.sal, self.dept)

    def search_emp(self, search):
        flag = 0
        for record in emp_details:
            if search in record[0]:
                print("Entry found:")
                print("ID: {}".format(record[0]))
                print("Name = {}".format(record[1]))
                print("Salary: {}".format(record[2]))
                print("Department: {}".format(record[3]))
                flag = 1
        if flag == 0:
            print("No employee found with ID = {}".format(search))
    

emp_details = []
n = int(input("How many employees:"))
for i in range(n):
    Id = input("ID:")
    name = input("Name:")
    sal = input("Salary:")
    dept = input("Department:")
    emp = employee(Id, name, sal, dept)
    emp_details.append(emp.create_tuple())

print("All details entered successfully")
search = input("Enter the employee ID to search:")
emp.search_emp(search)

print("\nAll the employees:")
for record in emp_details:
    print(record)
        
