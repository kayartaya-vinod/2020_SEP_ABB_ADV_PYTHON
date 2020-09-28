import ex03


class Salesman(ex03.Employee):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.commission = kwargs.get('commission', 0)

    # getter/accessor/readable property called 'commission'
    @property
    def commission(self): return self.__commission

    # setter/mutator/writable property called 'commission'
    @commission.setter
    def commission(self, value): self.__commission = value  # TBD: validation

    def __str__(self):
        return f'Salesman ({super().__str__()}, Commission={self.commission})'


def main():
    s1 = Salesman(name='John', email='john@xmpl.com', commission=2000)
    print(s1)


if __name__ == '__main__':
    main()