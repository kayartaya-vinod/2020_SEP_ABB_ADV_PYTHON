import time
import multiprocessing as mp


def hello():
    print('hello')
    time.sleep(1)  # simulating an io operation (ex: load file, read from socket, read from db, ..)
    print('bye')


def main():
    s = time.perf_counter()
    # p1 = mp.Process(target=hello)
    # p2 = mp.Process(target=hello)
    # p3 = mp.Process(target=hello)
    #
    #
    # p1.start()
    # p2.start()
    # p3.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()
    for _ in range(3):
        hello()

    e = time.perf_counter() - s
    print(f'All jobs done in {e} seconds.')




if __name__ == '__main__':
    main()
