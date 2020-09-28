def hello(name, city):
    print(f'name = {name}, city={city}')


def add(*args):
    # args --> tuple
    return sum(args)


def print_info(**kwargs):
    # kwargs --> dict
    print(kwargs)


if __name__ == '__main__':
    hello(city='Shivamogaa', name='Vinod')
    print(add(100, 200, 300, 10, 20, 30))
    print_info(name='Vinod', age=47)
    print_info(x=10, y=20, z=40)