### Multithreading -> Doing multiple tasks at the same time instead of waiting for one to finish.
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
## eg. Request sent → waiting → data arrives → process. During waiting: CPU is idle, time is wasted
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

##create 2 threads -> Threads share the same memory space but execute independently with separate stacks(local variable).
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
## start the thread -> When one thread goes for I/O wait, other thread will get executed
t1.start()
t2.start()

### Wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)

# Two threads run print_numbers() and print_letter() concurrently.
# time.sleep() simulates I/O wait, join() waits for both threads to finish, and total time shows parallel execution.