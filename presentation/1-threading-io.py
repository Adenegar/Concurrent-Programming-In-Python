import threading
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=count)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")