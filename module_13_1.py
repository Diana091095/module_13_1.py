import asyncio
import time


async def start_strongman(name, power):
    # st = time.time()
    print(f'Силач {name} начал соревнования.')
    number_ball = [x+1 for x in range(5)]
    for num_ball in number_ball:
        await asyncio.sleep(1 / power) #(среднее 3,4,5)
        print(f'Силач {name} поднял {num_ball} шар.')
    print(f'Силач {name} закончил соревнования.')
    # fn = time.time()
    # print(f'{round(fn - st, 2)} время соревнования для игрока {name}')

async def start_tournament():
    task = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task
    await task2
    await task3

start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f'{round(finish - start, 2)} время соревнования')