'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing # Provides support for creating multiple processes
import math
import sys # Allows interaction with Python runtime settings.
import time

# Increase the maximum number of digits for integer conversion into string(printing/logging)
sys.set_int_max_str_digits(100000)
## Python limits how many digits an integer can have when converting to string.
## print(f"Factorial of {number} is {result}") -> without increasing the limit → ❌ crash


## function to compute factorials of a given number 
def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__": # Prevents infinite child-process creation on Windows & macOS.
    numbers=[5000,6000,700,8000]

    start_time=time.time()

    ##create a pool of worker processes
    ## Number of processes = number of CPU cores (by default).
    ## with ensures: processes start properly, processes terminate cleanly
    with multiprocessing.Pool() as pool: 
        results=pool.map(computer_factorial,numbers) ##pool.map distributes tasks across processes in parallel
        ## Sends each value from numbers to a separate process.
        ## Each process runs computer_factorial(number) independently.Executes truly in parallel
        ## Returns results in the same order as input. Output -> results = [5000!, 6000!, 700!, 8000!]

    end_time=time.time()

    print(f"Results: {results}") ## return type of results(pool.map) is "List"
    print(f"Time taken: {end_time - start_time} seconds")

