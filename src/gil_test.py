#!/usr/bin/env python3
# Import necessary modules
import sys
import sysconfig
import math
import time
from threading import Thread
from multiprocessing import Process

# Define a decorator to measure function execution time
def time_taken(func):
   def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function {func.__name__!r} took {execution_time:.4f} seconds to execute.")
        return result
   return wrapper

# Define a compute-intensive task function
def compute_intensive_task(num):
   return math.factorial(num)

# Define single-threaded task function
@time_taken
def single_threaded_task(nums):
   for num in nums:
        compute_intensive_task(num)

# Define multi-threaded task function
@time_taken
def multi_threaded_task(nums):
    threads = []

    # Create len(nums) threads
    for num in nums:
        thread = Thread(target=compute_intensive_task, args=(num,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Define multi-processing task function
@time_taken
def multi_processing_task(nums):
    processes = []

    # Create len(nums) processes
    for num in nums:
        process = Process(target=compute_intensive_task, args=(num,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

# Define the main function
def main():
    print(f"Python Version: {sys.version}")

    # Check GIL status
    py_version = float(".".join(sys.version.split()[0].split(".")[0:2]))
    status = sysconfig.get_config_var("Py_GIL_DISABLED")

    if py_version >= 3.13:
        status = sys._is_gil_enabled()
    if status is None:
        print("GIL cannot be disabled for Python version <= 3.12")
    if status == 0:
        print("GIL is currently disabled")
    if status == 1:
        print("GIL is currently active")

    nums = [300001, 300001, 300001, 300001, 300001, 300001]

    # Run single-threaded task
    single_threaded_task(nums)

    # Run multi-threaded task
    multi_threaded_task(nums)

    # Run multi-processing task
    multi_processing_task(nums)

# Call the main function
if __name__ == "__main__":
    main()
