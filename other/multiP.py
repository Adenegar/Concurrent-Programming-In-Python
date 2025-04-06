from multiprocessing import Process, Lock, set_start_method
import math
import time

def cpu_bound_work(num):
    return math.factorial(num + 10)

def run_process(lock, process_id):
    # Run a computation and display its result using a lock for safe printing.
    result = cpu_bound_work(process_id)
    lock.acquire()
    try:
        print(f'Process {process_id}: Computation result is {result}')
    finally:
        lock.release()

if __name__ == '__main__':
    start_time = time.perf_counter()

    # 1. Set start method for processes
    try:
        set_start_method('fork')  # Use copy-on-write; avoids spawning issues
    except RuntimeError:
        pass

    # 2. Start Processes: pass in lock and process number
    lock = Lock()
    processes = []
    for num in range(100):
        p = Process(target=run_process, args=(lock, num))
        processes.append(p)
        p.start()

    # 3. End Processes when they've finished
    for p in processes:
        p.join()


    elapsed = time.perf_counter() - start_time
    print(f'With multiprocessing executed in {elapsed:0.2f} seconds.')
