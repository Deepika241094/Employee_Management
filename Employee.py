import json
class Employee:
    def __init__(self, name, employee_id, title, department):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")

    def __str__(self):
        return f"{self.name} - {self.employee_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]

    def list_employees(self):
        for employee in self.employees:
            print(employee)

class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        del self.departments[department_name]

    def display_departments(self):
        for department_name, department in self.departments.items():
            print(f"Department: {department_name}")
            department.list_employees()
            print()

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            data = {
                'departments': {
                    name: [str(emp) for emp in dept.employees]
                    for name, dept in self.departments.items()
                }
            }
            json.dump(data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for department_name, employees in data['departments'].items():
                department = Department(department_name)
                for emp_str in employees:
                    name, employee_id = emp_str.split(' - ')
                    employee = Employee(name, int(employee_id), '', department_name)
                    department.add_employee(employee)
                self.add_department(department)

def print_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Departments")
    print("4. Save Data to File")
    print("5. Load Data from File")
    print("6. Exit")

# Example usage
if __name__ == "__main__":
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter employee name: ")
            emp_id = int(input("Enter employee ID: "))
            department_name = input("Enter department name: ")

            if department_name not in company.departments:
                print(f"Error: Department '{department_name}' does not exist.")
                continue

            employee = Employee(name, emp_id, '', department_name)
            company.departments[department_name].add_employee(employee)
            print(f"Employee {name} added to {department_name}.")

        elif choice == '2':
            emp_id = int(input("Enter employee ID to remove: "))

            for department in company.departments.values():
                department.remove_employee(emp_id)

            print(f"Employee with ID {emp_id} removed from all departments.")

        elif choice == '3':
            company.display_departments()

        elif choice == '4':
            filename = input("Enter filename to save data: ")
            company.save_to_file(filename)
            print("Data saved successfully.")

        elif choice == '5':
            filename = input("Enter filename to load data: ")
            company.load_from_file(filename)
            print("Data loaded successfully.")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")