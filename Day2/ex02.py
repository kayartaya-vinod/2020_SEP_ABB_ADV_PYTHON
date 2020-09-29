def absolute(fn):  # <--- fn is a reference to factorial
    def inner(n):  # <--- n is the argument to the function
        n = n if n >= 0 else -n  # <--- what we are "decorating"
        return fn(n)

    return inner


@absolute
def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


def main():
    nums = [9, 5, -10, 3, -7, 12]
    factorials = [factorial(n) for n in nums]

    fcts = [absolute(factorial)(n) for n in nums]
    print(nums)
    print(factorials)
    print(fcts)


if __name__ == '__main__':
    main()
