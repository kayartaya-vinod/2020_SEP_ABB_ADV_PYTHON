def int_param(fn):
    def inner(param):
        # add decoration here
        if type(param) != int:
            raise TypeError(f'Expected int, but got {type(param)} ---> {param}')
        return fn(param)

    return inner


@int_param
def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


@int_param
def square(num):
    return num*num


def main():
    n = 'sss'
    f = factorial(n)
    print(f'Factorial {n} is {f}')
    n = 'ten'
    s = square(n)
    print(f'Square {n} is {s}')


if __name__ == '__main__':
    main()
