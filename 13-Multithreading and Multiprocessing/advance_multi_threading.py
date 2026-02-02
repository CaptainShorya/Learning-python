### Multithreading With Thread Pool Executor
## ThreadPoolExecutor manages a fixed number of threads and automatically assigns tasks to them, which is ideal for I/O-bound work.
from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1) ## stimulates (I/O-bound behavior)
    return f"Number :{number}"

numbers=[1,2,3,4,5,6,7,8,9,0,1,2,3] ## Each number represents one independent task,Tasks can run in any order internally, but results stay ordered

with ThreadPoolExecutor(max_workers=3) as executor: ## Creates 3 threads only,Threads are reused (not created every time)
    results=executor.map(print_number,numbers) ##It applies the given function to each item in an iterable(here it is list) using threads from the pool and returns the results.
    ## Each element (numbers) passed one-by-one and becomes the argument to print_number
    ## result is an iterator and results appear in the same order as input, not execution order

for result in results:
    print(result)