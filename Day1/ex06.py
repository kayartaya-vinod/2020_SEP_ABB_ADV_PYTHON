class Circle:

    PI = 3.1415  # immutable
    lst = []  # mutable

    def __init__(self, radius=0):
        self.radius = radius
        Circle.lst.append(radius)

    @property
    def radius(self): return self.__radius

    @radius.setter
    def radius(self, value): self.__radius = value

    @property
    def area(self):
        return Circle.PI * self.radius

    def print_lst():
        print(f'lst is {Circle.lst}')


def main():

    print(f'Circle.lst = {Circle.lst}')

    c1 = Circle(23.45)
    print(f'Circle.lst = {Circle.lst}')
    c2 = Circle(12.34)
    print(f'Circle.lst = {Circle.lst}')

    Circle.print_lst()
    # c1.print_lst()

    print(f'c1.lst == c2.lst is {c1.lst==c2.lst}')
    print(f'id(c1.lst) is {id(c1.lst)}')
    print(f'id(c2.lst) is {id(c2.lst)}')
    print(f'id(Circle.lst) is {id(Circle.lst)}')

    c1.a = 100
    c2.x = 200

    print(f'c1.area = {c1.area}')
    print(f'c2.area = {c2.area}')


if __name__ == '__main__':
    main()