def validate_params(*types):
    # this function is not a decorator
    # return value of this function (which should be a function) is the decorator
    def decorator(fn):  # <--- fn is the function on which the decorator is applied
        def inner(*args):  # <--- args is the arguments supplied to the function
            # do the actual decoration here
            # length of args must match length of types
            if len(args) != len(types):
                raise Exception('length of args must match length of types')

            # type of each argument must match corresponding type in types list
            for (i, t) in enumerate(types):
                if t != type(args[i]):
                    raise TypeError('types of arguments did not match expected types')

            return fn(*args)

        return inner

    return decorator


@validate_params(str, str)
def hello(name, city):
    print(f'Hello {name}, how\'s weather in {city}')


@validate_params(int)
def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


@validate_params(float, float, float, float)
def add(a, b, c, d):
    return sum([a, b, c, d])


def main():
    hello('Vinod', 'Bangalore')
    f = factorial(5)
    print(f'factorial of 5 is {f}')
    total = add(1.5, 2.2, 3.5, 4.5)
    print(f'Total = {total}')


if __name__ == '__main__':
    main()
