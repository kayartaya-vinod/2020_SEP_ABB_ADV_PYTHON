class Employee:
    # class state; shared across all objects
    employees = []

    def __init__(self, id, name, salary=25000):
        # object state; per object
        self.__id = id
        self.__name = name
        self.__salary = salary

    def __str__(self):
        return f'Id={self.__id}, Name={self.__name}, Salary=₹{self.__salary}'

    @classmethod
    def add_employee(cls, emp):
        cls.employees.append(emp)

    @classmethod
    def print_employees(cls):
        for e in cls.employees:
            print(e)

    # use static methods when a function make sense to be in this class,
    # but only works as utility (and does not need object/class state)
    @staticmethod
    def calculate_gross_salary(salary):
        # do some calculations and work on salary
        return salary * 1.3


def main():
    e1 = Employee(101, 'John Doe')
    e2 = Employee(102, 'Jane Doe')

    # 'Employee' is an object of 'type' (ex: in Java java.lang.Class, java.lang.Object)
    Employee.add_employee(e1)
    Employee.add_employee(e2)
    emp_class = Employee
    emp_class.add_employee(Employee(103, 'Harry Bosch'))

    Employee.print_employees()


if __name__ == '__main__':
    main()
