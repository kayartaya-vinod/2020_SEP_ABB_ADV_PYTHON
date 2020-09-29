def border(fn):
    def wrapee():
        print('*'*50)
        fn()  # executing the argument function (ex: hello)
        print('*'*50)

    return wrapee


@border
def hello():
    print('Hello, world!')


@border
def welcome():
    print('Welcome to Adv.Python')


def main():
    # new_hello = border(hello)
    # new_hello()
    # border(welcome)()
    hello()
    welcome()


if __name__ == '__main__':
    main()
