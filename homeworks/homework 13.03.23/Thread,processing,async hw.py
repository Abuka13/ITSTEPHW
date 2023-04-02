import requests
import threading
import multiprocessing
import asyncio
import json
import time

def time_measure(func):
    def wrapper(*args,**kwargs):
        time_start = time.perf_counter()
        result = func()
        time_stop = time.perf_counter()
        print("elapsed time: ", round(time_stop - time_start, 5))
        return result
    return wrapper
def processing_json_place():
    with open(f'json_processing.json', 'w') as file:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        todos = json.loads(response.text)
        for i in range(1,10+1):
            file.write(str(todos[i - 1:i]))
def threading_json_place():
    with open(f'json_threading.json', 'w') as file:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        todos = json.loads(response.text)
        for i in range(1,10+1):
            file.write(str(todos[i - 1:i]))
async def async_json_place():
    # await asyncio.sleep(1.0)
    # return None
    with open(f'async.json', 'w') as file:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        todos = json.loads(response.text)
        for i in range(1, 10 + 1):
            file.write(str(todos[i - 1:i]))

@time_measure
def processing_json():
    new_process_list = []
    for i in range(1,10+1):
        new_process_list.append(multiprocessing.Process(target=processing_json_place(), args=(), kwargs={}))
    for i in new_process_list:
        i.start()
    for i in new_process_list:
        i.join()
@time_measure
def threading_json():
    new_thread_list = []
    for i in range(1, 10 + 1):
        new_thread_list.append(threading.Thread(target=threading_json_place(), args=(), kwargs={}))
    for i in new_thread_list:
        i.start()
    for i in new_thread_list:
        i.join()
@time_measure
def async_json():
    async def create_tasks():  # coroutines
        await asyncio.gather(*[async_json_place() for _ in range(1, 10 + 1)])

    asyncio.run(create_tasks())
    asyncio.run(create_tasks())
if __name__ == "__main__":
    processing_json()
    threading_json()
    async_json()

