class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.city = kwargs.get('city')

        print('creating an instance of Person class')

    def show(self):
        print('showing details of person...')

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, value): self.__name = value

    @property
    def city(self): return self.__city

    @city.setter
    def city(self, value): self.__city = value


def hello():
    pass


# the below listed code creates a class called 'Employee', with no base types, and no attributes
Employee = type('Employee', (Person,), {'id': 101, 'name': 'John'})


def main():
    p1 = Person()
    print(f'type(p1) is {type(p1)}')
    print(f'type(Person) is {type(Person)}')
    print(f'type(type) is {type(type)}')
    print(f'type(hello) is {type(hello)}')
    e1 = Employee()
    e1.name = 'Scott'
    e1.city = 'Paris'
    e1.show()
    print(f'attrs in e1 are: {dir(e1)}')
    print(f'type(e1.city) is {type(e1.city)}')


if __name__ == '__main__':
    main()
