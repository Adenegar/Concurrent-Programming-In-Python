import time
import math

def cpu_bound_work(num):
    return math.factorial(num + 100000) % 29

def main():
    results = []
    for num in range(10):
        result = cpu_bound_work(num)
        results.append((num, result))
        print(f'Computation result is {result}')
    return results

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f'Without multiprocessing executed in {elapsed:0.2f} seconds.')
