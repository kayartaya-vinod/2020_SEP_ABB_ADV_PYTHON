class Triangle:

    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    # getter/setter for '__base'
    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        if type(value) not in (int, float):
            raise TypeError('Only numbers are allowed for base')
        if value < 0:
            raise ValueError('Negative value are not allowed for base')
        self.__base = value

    # getter/setter for '__height'
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in (int, float):
            raise TypeError('Only numbers are allowed for height')
        if value < 0:
            raise ValueError('Negative value are not allowed for height')
        self.__height = value

    # readonly property (getter) for 'area'
    @property
    def area(self): return .5 * self.base * self.height

    def __str__(self):
        return f'Triangle (Base={self.base}, Height={self.height}, Area={self.area})'


def main():
    t1 = Triangle()
    t1.base = 5.5
    t1.height = 4.4
    print(t1)
    # t1.area = 222 ---> error; area is a readonly property
    print(f'Area of triangle with base {t1.base} and height of {t1.height} is {t1.area}')
    t2 = Triangle(12, 34)
    print(t2)


if __name__ == '__main__':
    main()
