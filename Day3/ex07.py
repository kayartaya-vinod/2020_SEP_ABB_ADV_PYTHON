import asyncio
import time


async def hello():
    print('Hello.')
    await asyncio.sleep(1)
    # time.sleep(1)
    print('Bye!')


async def main():
    await asyncio.gather(hello(), hello(), hello(), hello())


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    e = time.perf_counter() - s
    print(f'Completed all tasks in {e} seconds.')
