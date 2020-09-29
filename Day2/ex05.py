class TitleCaseParams(object):
    def __init__(self, fn):
        # fn is the function on which decorator is applied
        self.__fn = fn

    # this function gets called when the function on which the decorator
    # is applied is executed (ex: in main() method)
    def __call__(self, *args, **kwargs):
        # do the actual decoration here

        def title_case(s):
            return s[0].upper() + s[1:].lower() if type(s) is str else s

        new_args = []
        for arg in args:
            new_args.append(title_case(arg))

        for key in kwargs:
            kwargs[key] = title_case(kwargs[key])

        return self.__fn(*new_args, **kwargs)


@TitleCaseParams
def hello(name, city):
    print(f'Hello {name}, how\'s weather in {city}?')


def main():
    hello('vinod', 'BANGALORE')
    hello('VINOD', city='BANGALORE')
    hello(city='bangaLORE', name='VINOD')


if __name__ == '__main__':
    main()
