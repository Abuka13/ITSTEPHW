import random
import requests  # todo синхронная (последовательная)
import aiohttp  # todo асинхронная (параллельная)
import time
import threading
import multiprocessing
import asyncio
import concurrent.futures
print(1)
print(2)




print(3)

#TODO Процессы потоки
# sync VS async VS threading VS multiprocessing

# sync =                1 процесс: 1 поток
# threading =           1 процесс: N поток
# multiprocessing =     N процесс: N поток
# async =               1 процесс: 1 поток #топ4
url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
def time_measure(func):
    def wrapper(*args,**kwargs):
        time_start = time.perf_counter()
        result = func()
        time_stop = time.perf_counter()
        print("elapsed time: ", round(time_stop - time_start, 5))
        return result
    return wrapper

def sync_download_one_image():
    time.sleep(1.0)
    response = requests.get(url=url, headers=headers)



    with open(f"image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
        opened_file.write(response.content)
@time_measure
def sync_download_mass_image():
    # загрузка 10 картинок в этом потоке
    for i in range(1, 10 + 1):
        sync_download_one_image()



#TODO Как загрузить сразу 10 картинок
@time_measure
def threading_download_mass_image():
    # new_thread = threading.Thread(target=sync_download_one_image,args=(),kwargs={})
    # new_thread.start()
    # new_thread.join()
    new_thread_list = []
    for i in range(1, 10 + 1):
        new_thread_list.append(threading.Thread(target=sync_download_one_image,args=(),kwargs={}))
    print(new_thread_list)
    for i in new_thread_list:
        i.start()
    for i in new_thread_list:
        i.join()
    # # # todo чтобы не перенагрузить систему и выбрать "оптимальное количество потоков"
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     for i in range(1, 10 + 1):
    #         executor.submit(sync_download_one_image)
async def async_download_one_image():
    # await asyncio.sleep(1.0)
    # return None
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response_obj:
            data = await response_obj.read()
            # todo sync! AIOFILES
            with open(f"image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
                opened_file.write(data)
if __name__ == "__main__":
    # threading_download_mass_image()
    # sync_download_mass_image()            # elapsed time:  10.05191
    # threading_download_mass_image()       # elapsed time:  1.0152
    # processing_download_mass_image()      # elapsed time:  1.31037
    asyncio.run(async_download_one_image())
    pass