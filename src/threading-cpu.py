import math
import time
import threading

def cpu_bound_work(num):
    return math.factorial(num + 100000) % 29

def run_thread(lock, thread_id):
    # Run a computation and display its result using a lock for safe printing.
    result = cpu_bound_work(thread_id)
    lock.acquire()
    try:
        print(f'Thread {thread_id}: Computation result is {result}')
    finally:
        lock.release()

if __name__ == '__main__':
    start_time = time.perf_counter()

    lock = threading.Lock()
    threads = []
    for num in range(10):
        t = threading.Thread(target=run_thread, args=(lock, num))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start_time
    print(f'With threading executed in {elapsed:0.2f} seconds.')
