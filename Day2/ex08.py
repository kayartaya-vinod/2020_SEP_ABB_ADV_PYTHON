import multiprocessing as mp
import os

# shared resource across multiple processes
data = [12, 3, 49, 51, 39, 9, 45]
result = []


def square_nums(nums):
    global result

    for (i, n) in enumerate(nums):
        result.append(n * n)

    print(f'[{os.getpid()}], inside square_nums(), result is {result}')


def main():
    global result, data
    p1 = mp.Process(target=square_nums, args=[data])
    p1.start()

    p1.join()
    print(f'[{os.getpid()}], inside main(), result is {result}')


if __name__ == '__main__':
    main()
