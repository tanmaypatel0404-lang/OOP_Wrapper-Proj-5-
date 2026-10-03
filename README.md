# 👨‍💼 Employee Management System

## 📌 Project Overview

The **Employee Management System** is a beginner-friendly Python project developed using **Object-Oriented Programming (OOP)** concepts.

The program allows users to create and manage different types of people, including **Person, Employee, and Manager**. It uses a simple menu-driven system where the user can create objects and display their details.

This project is mainly designed to demonstrate important Python OOP concepts such as **Classes, Objects, Inheritance, Encapsulation, Polymorphism, Constructors, Method Overriding, `super()`, and Destructors**.

---

## 🎯 Project Objectives

The main objectives of this project are:

* To understand the basic structure of Python classes and objects.
* To demonstrate inheritance between different classes.
* To understand how private attributes work in Python.
* To practice constructors and methods.
* To understand method overriding.
* To demonstrate the use of `super()`.
* To create a simple menu-driven application using OOP.

---

## ✨ Features

### 👤 Create a Person

The program allows the user to create a `Person` by entering:

* Name
* Age

The person's details can then be displayed using the `display()` method.

### 👨‍💼 Create an Employee

The program allows the user to create an `Employee` by entering:

* Name
* Age
* Employee ID
* Salary

Employee ID and salary are stored using private attributes.

### 👔 Create a Manager

A Manager is a specialized type of Employee.

The user can enter:

* Name
* Age
* Employee ID
* Salary
* Department

The Manager class inherits the properties and methods of the Employee class.

### 📋 Show Details

The program provides a separate option to display the details of:

1. Person
2. Employee
3. Manager

If an object has not been created, the program displays an appropriate message.

### 🚪 Exit

The user can exit the program by selecting the **Exit** option.

---

# 🧠 OOP Concepts Used

## 1. Classes and Objects

A **class** is a blueprint used to create objects.

The project contains three main classes:

```python
class Person:
```

```python
class Employee(Person):
```

```python
class Manager(Employee):
```

Objects are created from these classes:

```python
person = Person(name, age)
```

```python
employee = Employee(name, age, employee_id, salary)
```

```python
manager = Manager(name, age, employee_id, salary, department)
```

---

## 2. Inheritance

Inheritance allows one class to use the properties and methods of another class.

The project follows this inheritance structure:

```text
Person
  ↓
Employee
  ↓
Manager
```

`Employee` inherits from `Person`:

```python
class Employee(Person):
```

`Manager` inherits from `Employee`:

```python
class Manager(Employee):
```

This avoids writing the same code repeatedly.

---

## 3. Encapsulation

Encapsulation is used to protect data inside a class.

In the `Employee` class, Employee ID and salary are private attributes:

```python
self.__employee_id = employee_id
self.__salary = salary
```

The double underscore `__` is used to make these attributes private.

The program uses getter and setter methods to access and modify them.

### Getter

```python
def get_salary(self):
    return self.__salary
```

### Setter

```python
def set_salary(self, salary):
    self.__salary = salary
```

This provides controlled access to the employee's information.

---

## 4. Polymorphism

Polymorphism means that the same method name can behave differently in different classes.

The `display()` method is defined in the `Person` class:

```python
def display(self):
```

It is then overridden in the `Employee` class:

```python
def display(self):
```

And again in the `Manager` class:

```python
def display(self):
```

Each class adds its own information while using the parent class's display functionality.

---

## 5. Method Overriding

The `Employee` and `Manager` classes override the `display()` method of their parent classes.

For example:

```python
class Employee(Person):

    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)
```

The Manager class further extends it:

```python
class Manager(Employee):

    def display(self):
        super().display()
        print("Department:", self.department)
```

This allows each class to display its specific information.

---

## 6. Constructor

The `__init__()` method is a constructor in Python.

It is automatically called when an object is created.

For example:

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

When we create:

```python
person = Person("Rahul", 25)
```

the constructor automatically stores the name and age.

---

## 7. `super()` Function

The `super()` function is used to access methods or constructors from the parent class.

For example, Employee uses:

```python
super().__init__(name, age)
```

This calls the constructor of the `Person` class.

Similarly, Manager uses:

```python
super().__init__(name, age, employee_id, salary)
```

This calls the constructor of the Employee class.

The `super()` function helps reduce duplicate code.

---

## 8. Destructor

The Employee class contains a destructor:

```python
def __del__(self):
    print("Employee object deleted")
```

The `__del__()` method can be called when an object is being destroyed.

It is included in this project to demonstrate the concept of a **destructor in Python**.

---

# 🏗️ Class Structure

The project uses three classes.

### 👤 Person

Stores basic personal information:

```text
Person
├── name
└── age
```

### 👨‍💼 Employee

Inherits from Person and adds employee information:

```text
Employee
├── name
├── age
├── employee_id
└── salary
```

### 👔 Manager

Inherits from Employee and adds department information:

```text
Manager
├── name
├── age
├── employee_id
├── salary
└── department
```

---

# 📋 Program Menu

When the program starts, the user sees:

```text
Choose an operation:

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
```

The user selects an option by entering its number.

---

# 🔄 Program Flow

The basic flow of the program is:

```text
Start
  ↓
Display Menu
  ↓
Choose Operation
  ↓
 ┌──────────────────────┐
 │ 1. Create Person     │
 │ 2. Create Employee   │
 │ 3. Create Manager    │
 │ 4. Show Details      │
 │ 5. Exit              │
 └──────────────────────┘
  ↓
Perform Selected Operation
  ↓
Return to Menu
  ↓
Exit when option 5 is selected
```

The `while True` loop keeps the program running until the user selects **Exit**.

---

# 💻 Technologies Used

| Technology                | Purpose                                          |
| ------------------------- | ------------------------------------------------ |
| 🐍 Python                 | Programming language                             |
| 🧱 OOP                    | Organizing the program using classes and objects |
| 🔁 While Loop             | Keeping the menu running                         |
| 🔀 Conditional Statements | Handling different menu choices                  |
| 📝 User Input             | Taking information from the user                 |

---

# ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Save the Program

Save the Python file with a name such as:

```text
employee_management.py
```

### Step 3: Run the Program

Open a terminal in the project folder and run:

```bash
python employee_management.py
```

### Step 4: Use the Menu

Enter the number corresponding to the operation you want to perform.

---

# 🧪 Example

### Creating an Employee

```text
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice: 2

Enter Name: Rahul
Enter Age: 25
Enter Employee ID: E101
Enter Salary: 35000

Employee created successfully.
```

### Displaying Employee Details

```text
1. Person
2. Employee
3. Manager

Choose details to show: 2

Name: Rahul
Age: 25
Employee ID: E101
Salary: 35000.0
```

---

# 📚 What I Learned From This Project

This project provides practical understanding of:

* How to create Python classes.
* How to create and use objects.
* How constructors work.
* How inheritance works.
* How multiple levels of inheritance can be created.
* How encapsulation can protect data.
* How getters and setters work.
* How method overriding works.
* How polymorphism is implemented.
* How `super()` is used.
* How destructors work.
* How to build a menu-driven Python application.

---

# 🚀 Future Improvements

The project can be extended with additional features such as:

* Store multiple employees.
* Search employees by Employee ID.
* Update employee information.
* Delete employees.
* Calculate salary or bonuses.
* Add different employee roles.
* Save employee data to a file.
* Connect the system with a database.
* Add input validation and error handling.

---

# 👨‍💻 Project Type

**Beginner Python OOP Project**

This project is suitable for students and beginners who are learning **Object-Oriented Programming in Python**.

---

## ⭐ Conclusion

The **Employee Management System** is a simple practical project that demonstrates how OOP can be used to organize real-world information.

By using **Person → Employee → Manager** inheritance, the project shows how classes can be connected and reused while keeping the code organized and easy to understand.

> 🐍 **Built with Python | Focused on Object-Oriented Programming**
