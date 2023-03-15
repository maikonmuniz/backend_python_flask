import asyncio
import aiohttp
import datetime

_url = 'http://localhost:5000/message'
data = {
	"message": "Olá tudo bem? Que saudades de vc!",
	"zipcode": "13207500"
}

async def fetch(session, url):
    async with session.post(url, json=data) as response:
        return await response.json()

async def call_api(i):
    print(f'calling{i}')
    print(datetime.datetime.now())
    async with aiohttp.ClientSession() as session:
        res = await fetch(session, _url)
        print(datetime.datetime.now())
        print(f'api call finished...{i} -> {res}')
        return res

async def main():
    print(datetime.datetime.now())
    print('calling multiple APIs')
    tasks = []
    for i in range(5):
        tasks.append(call_api(i))
        print(f'api call posted...{i}')
    await asyncio.wait(tasks)
    print(f'all APIs calls finished')
    print(datetime.datetime.now())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
