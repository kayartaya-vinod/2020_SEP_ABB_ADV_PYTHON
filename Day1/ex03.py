from ex00 import Person


class Employee(Person):

    # the inherited __init__ is hidden or overridden by the newly defined __init__
    def __init__(self, **kwargs):
        # in other OO languages, like c++/Java/C# automatic execution of the
        # super/base class constructor takes place.

        # in Python, this constructor must make an explicit call to base/super constructor
        super().__init__(**kwargs)
        # Person.__init__(self, **kwargs)
        self.salary = kwargs.get('salary', 35000)  # executing the salary.setter function

    def __str__(self):
        return f'Employee ({super().__str__()}, Salary={self.salary})'

    @property
    def salary(self): return self.__salary

    @salary.setter
    def salary(self, value): self.__salary = value  # TBD: validation of value


def main():
    e1 = Employee(name='John', age=22)
    print(f'attributes in e1 are {dir(e1)}')
    print(e1)  # e1.__str__()

    e1.__init__(name='scott', salary=22200)
    print(e1)


if __name__ == '__main__':
    main()
