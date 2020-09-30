import requests
import time
from aiohttp import ClientSession
import asyncio


async def aio_fetch(keyword):
    url = f'http://www.omdbapi.com/?s={keyword}&apikey=aa9e49f'
    async with ClientSession() as session, session.get(url) as res:
        return await res.read()


def fetch(keyword):
    url = f'http://www.omdbapi.com/?s={keyword}&apikey=aa9e49f'
    return requests.get(url).content


keywords = ['iron', 'spider', 'avengers', 'war']


async def print_when_done(tasks):
    for result in asyncio.as_completed(tasks):
        print(await result)


async def async_requests():
    tasks = [aio_fetch(kw) for kw in keywords]
    await print_when_done(tasks)


def main():
    s = time.perf_counter()

    for kw in keywords:
        result = fetch(kw)
        print(result)

    e = time.perf_counter() - s
    print(f'Total time taken for all requests = {e} seconds.')
    print()

    s = time.perf_counter()
    asyncio.run(async_requests())
    e = time.perf_counter() - s
    print(f'Total time taken for all requests = {e} seconds.')


if __name__ == '__main__':
    main()
