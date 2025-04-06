from multiprocessing import Pool, Lock, set_start_method
import time

# Global variable to hold the lock in worker processes
print_lock = None

def init(lock):
    # Initialize the global lock for each worker
    global print_lock
    print_lock = lock

def cpu_bound_work(param):
    # Abstracted CPU-intensive computation (details hidden for clarity)
    total = 0
    for j in range(10_000_000):
        total += (j % (param + 1)) ** 2
    return total

def run_task(task_id):
    # Run a computation and display its result using a global lock.
    result = cpu_bound_work(task_id)
    print_lock.acquire()
    try:
        print(f'Task {task_id}: Computation result is {result}')
    finally:
        print_lock.release()
    return result

if __name__ == '__main__':
    start_time = time.perf_counter()

    # Set start method for processes
    try:
        set_start_method('fork')  # Use copy-on-write; avoids spawning issues
    except RuntimeError:
        pass

    # Create a lock and initialize a pool with it
    lock = Lock()
    with Pool(processes=100, initializer=init, initargs=(lock,)) as pool:
        # Map the work to the pool using process IDs 0 through 9.
        pool.map(run_task, range(1000))

    elapsed = time.perf_counter() - start_time
    print(f'With process pool executed in {elapsed:0.2f} seconds.')