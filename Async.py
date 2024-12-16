# async io for multiple tasks concurrent handling
# threads for tasks that share data and run simultaneously
# processes for cpu heavy tasks in parallel across multiple cores

import asyncio
import time
# In async io , event loop distributes and manages tasks

# Another coroutine
async def fetch_data(delay,id):
    print("Fetching data...")
    #time.sleep(delay)
    await asyncio.sleep(delay=delay)
    print("Data Fetched")
    return {"data":"Some data", "id":id}

#couroutine function
async def main():
    print("start of main coroutine")
    
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 10)

    start1 =  time.localtime().tm_min*60 + time.localtime().tm_sec
    result1 = await task1         # it starts execution
    end1 =  time.localtime().tm_min*60 + time.localtime().tm_sec
    print(result1,  f"\n took {end1 - start1} seconds")

    result2 = await task2
    end2 = time.localtime().tm_min*60 + time.localtime().tm_sec
    print(result2, f"\n took {end2 - start1} seconds")
    

    # so it took total 4 sec , so there was no performance benefit

    task1 = asyncio.create_task(fetch_data(2,1))
    task2 = asyncio.create_task(fetch_data(2,2))
    task3 = asyncio.create_task(fetch_data(2,3))

    start3 = time.localtime().tm_min*60 + time.localtime().tm_sec
    result1 = await task1
    result2 = await task2
    result3 = await task3

    end3 = time.localtime().tm_min*60 + time.localtime().tm_sec
    print("\n", result1, result2, result3, f" took {end3 - start3} seconds" ) #time.sleep took all 6 sec but async.sleep took 3 sec for all 3 tasks
    print("End of main coroutine")

#coroutine obj needs to be awaited (inside the async function) to be executed

# run the main coroutine , starts event loop
asyncio.run(main()) # main function returns Coroutine obj



