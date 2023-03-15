import time
import asyncio
import datetime

async def count_until_async(secs):
    print(f'counting until {secs}')
    await asyncio.sleep(secs)
    print(datetime.datetime.now())
    print(f'finished counting until {secs}')

async def main():
    print('calling multiple counters')
    print(datetime.datetime.now())
    tasks = []
    for i in range(10):
        tasks.append(count_until_async(i))

    await asyncio.wait(tasks)

    print('game is finished, thanks for joining!')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()