# Задача "Асинхронные силачи"

from time import time, sleep
import asyncio


async def start_strongman(name, power):
	print(f'Силач {name} начал соревнования.')
	# ball_number = 0
	for ball_number in range(1, 6):
		await asyncio.sleep(5/power)
		print(f'Силач {name} поднял шар {ball_number}')
	print(f'Силач {name} закончил соревнованияю.')
async def start_tournament():
	task1 = asyncio.create_task(start_strongman("Hercules", 10))
	task2 = asyncio.create_task(start_strongman('Kochubei', 15))
	task3 = asyncio.create_task(start_strongman('Goliaf', 20))
	await task1
	await task2
	await task3

asyncio.run(start_tournament())
