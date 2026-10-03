print(" Employee Management System ")


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def __init__(self, name, age, employee_id="", salary=0):
        super().__init__(name, age)

        self.__employee_id = employee_id
        self.__salary = salary

    def get_id(self):
        return self.__employee_id

    def set_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        print("Employee object deleted")


class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


# Objects
person = None
employee = None
manager = None


while True:

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)

        print("Person created successfully.")


    elif choice == 2:

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, employee_id, salary)

        print("Employee created successfully.")


    elif choice == 3:

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, employee_id, salary, department)

        print("Manager created successfully.")


    elif choice == 4:

        print("\n1. Person")
        print("2. Employee")
        print("3. Manager")

        option = int(input("Choose details to show: "))

        if option == 1:

            if person != None:
                person.display()
            else:
                print("Person not created.")


        elif option == 2:

            if employee != None:
                employee.display()
            else:
                print("Employee not created.")


        elif option == 3:

            if manager != None:
                manager.display()
            else:
                print("Manager not created.")


        else:
            print("Invalid choice.")


    elif choice == 5:

        print("Exiting the system. Goodbye!")
        break


    else:
        print("Invalid choice.")
