from quart import Quart
import asyncio

async def count_until_async(secs):
    print(f'counting until {secs}')
    await asyncio.sleep(secs)
    print(f'finished counting until {secs}')

async def main():
    print('calling multiple counters')
    tasks = []
    for i in range(10, 0, -1):
        tasks.append(count_until_async(i))

    await asyncio.wait(tasks)

    print('game is finished, thanks for joining!')

app = Quart('app')

@app.route('/')
async def index():
    await main()
    return 'hello'

app.run(host='localhost', port=5000)