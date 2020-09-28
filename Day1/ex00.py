class Person(object):

    # We are overriding the inherited __init__ function from the object class.
    # Python invokes this function, after the allocation of a new object space in the heap is done.
    # It passes the reference of the newly constructed object (in the heap) as the first argument,
    # which generally termed as 'self'. Using this 'self', we can add new attributes (like variables).
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.age = kwargs.get('age')
        self.__email = kwargs.get('email')

    def print_info(self):
        print(f'Name = {self.__name}')
        print(f'Age = {self.__age} years' )
        print(f'Email = {self.__email}')
        print()

    def __str__(self):
        return f'Person (Name={self.__name}, Age={self.__age}, Email={self.__email})'

    # getter/setter for 'age' property acting as proxy for __age
    # print(p1.age)  --> triggers the below defined function
    @property
    def age(self):
        return self.__age

    # p1.age = 55 ---> triggers the execution of the below defined function
    @age.setter
    def age(self, value):
        self.__age = value


def main():
    p1 = Person(name='Vinod', email='vinod@vinod.co', age=47)
    # RHS in the above line is an instruction to Python to allocate memory required for an object
    # of type Person, and then call the __init__() of the class Person. If the class does not have one,
    # then the inherited __init__() (from object class) will be invoked. Once this is done, Person() call
    # returns the reference of the newly constructed object.
    print(f'Id of p1 is {id(p1)}')
    print(f'type of p1 is {type(p1)}')
    print(f'Attributes of p1 are {dir(p1)}')

    # when calling a member function using an invoking object (ex: p1), the reference of the
    # invoking object itself is passed as an argument (implicitly)
    p1.print_info()
    p1.__age = 2000
    Person.print_info(p1)
    print(f'Attributes of p1 are {dir(p1)}')

    p2 = Person(name='Shyam', email='shyam@xmpl.com')
    p2.age = 48  # should change p2.__age; invokes a setter function
    print(p1)  # is equivalent to print(p1.__str__()) __str__() is implicitly called
    print(p2)
    print(f'p2.age is {p2.age}')  # should get p2.__age; invokes a getter function
    print(f'Attributes of p2 are {dir(p2)}')


# __name__ is built in global variable, that represents the name of the module.
# by default, it will have the name of the file, but in the module (file) that is currently
# being executed, it will have '__main__' as the name.
if __name__ == '__main__':
    main()
