class MyMetaClass(type):
    def __new__(mcs, *args):  # <-- args is always a tuple consisting of class_name, bases, attrs
        # print(f'args is {args}')
        class_name, bases, attrs = args
        if '__str__' not in attrs:
            raise Exception(f'__str__ is missing in {class_name} class, but required.')

        return type(class_name, bases, attrs)


class Person(metaclass=MyMetaClass):
    def __str__(self):
        return ''


class Employee(Person, metaclass=MyMetaClass):
    def __str__(self):
        return ''


def main():
    p1 = Person()
    print(p1)
    print(type(p1))
    print(dir(p1))


if __name__ == '__main__':
    main()
