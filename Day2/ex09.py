import multiprocessing as mp
import os


def square_nums(nums, result, total_squares):
    print(f'int square_nums, id(result) = P{id(result)}')
    total_squares.value = 0
    for (i, n) in enumerate(nums):
        result[i] = n * n
        total_squares.value += result[i]

    print(f'[{os.getpid()}], inside square_nums(), result is {result[:]}, total_squares is {total_squares.value}')


def main():
    data = [12, 3, 49, 51, 39, 9, 45]
    result = mp.Array('i', len(data))
    total_squares = mp.Value('i')

    print(f'in main(), id(result) = P{id(result)}')

    p1 = mp.Process(target=square_nums, args=[data, result, total_squares])
    p1.start()

    p1.join()
    print(f'[{os.getpid()}], inside main(), result is {result[:]}, total_squares is {total_squares.value}')


if __name__ == '__main__':
    main()
