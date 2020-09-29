import multiprocessing as mp
import os
import time


def fibo(num):
    a, b = -1, 1
    for _ in range(num):
        c = a + b
        print(f'pid={os.getpid()}, c={c}')
        a, b = b, c
        time.sleep(.25)


def main():

    p1 = mp.Process(target=fibo, args=[25])
    p1.start()

    print(f'inside main(), pid={os.getpid()}')
    fibo(10)

    p1.join()
    print('End of main()')


if __name__ == '__main__':
    main()
