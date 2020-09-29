import threading
import time
import os

# lock = threading.Lock()


class MyCustomThread(threading.Thread):
    def __init__(self, name, data):
        super().__init__()
        self.__name = name
        self.__data = data

    # every thread class must have a run() method
    # This is the very first function to be placed in the stack as a
    # stack frame, when the scheduler allocates a stack for this thread
    def run(self):
        # db connection is used over here
        for d in self.__data:
            # lock.acquire()
            print(f'[{os.getpid()}Processing the data {d} in thread {self.__name}')
            time.sleep(.5)
            # lock.release()


class PrintPounds(threading.Thread):

    def __init__(self):
        super().__init__()
        super().setDaemon(True)

    def run(self):
        while True:
            time.sleep(.5)
            print('#', end='')


def main():
    # db connection is open here
    print('starting main() method...')
    t1 = MyCustomThread('thread-0', ['vinod', 'shyam', 'harish', 'ramesh', 'john'])
    t2 = MyCustomThread('thread-1', [10, 20, 12, 395, 23, 56, 75])
    t3 = PrintPounds()

    t1.start()
    t2.start()
    t3.start()

    [t.join() for t in (t1, t2)]

    # db connection is closed over here
    print('main() method finished')


if __name__ == '__main__':
    main()
